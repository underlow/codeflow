#!/usr/bin/env python3
"""Restore this personal agterm setup; requires Python 3.11+, no dependencies."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tomllib

ROOT = Path(__file__).resolve().parent


def write(path, text, mode=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    if mode is not None:
        path.chmod(mode)


def render(text, home):
    return text.replace('@HOME@', str(home))


def set_feature(text, name, value):
    config = tomllib.loads(text)
    if config.get('features', {}).get(name) == value:
        return text
    block = re.search(r'^\[features\]\s*\n(.*?)(?=^\[|\Z)', text, re.M | re.S)
    line = '%s = %s' % (name, str(value).lower())
    if block:
        body = block.group(1)
        body, count = re.subn(r'^' + re.escape(name) + r'\s*=.*$', line, body, flags=re.M)
        if not count:
            body = body.rstrip() + '\n' + line + '\n'
        return text[:block.start(1)] + body + text[block.end(1):]
    return text.rstrip() + '\n\n[features]\n' + line + '\n'


def restore(home, ui_settings=False):
    home = home.resolve()
    # Validate readable configs before any writes. Do not collect account/auth files.
    codex = home / '.codex/config.toml'
    claude = home / '.claude/settings.json'
    codex_text = codex.read_text() if codex.exists() else ''
    tomllib.loads(codex_text)
    settings = json.loads(claude.read_text()) if claude.exists() else {}
    sources = [p for p in (ROOT / 'files').rglob('*') if p.is_file()]
    destinations = [home / p.relative_to(ROOT / 'files') for p in sources]
    destinations += [codex, claude, home / '.zshrc', home / '.config/yazi/keymap.toml', home / '.local/bin/agterm-activity.py']
    if ui_settings:
        destinations.append(home / 'Library/Application Support/agterm/settings.json')
    backup = home / '.config/agterm/codeflow-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True, mode=0o700)
    for path in set(destinations):
        if path.exists():
            target = backup / path.relative_to(home)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            target.chmod(0o600)
    for src, dest in zip(sources, destinations[:len(sources)]):
        text = render(src.read_text(), home)
        if src.name == 'keymap.conf' and dest.exists():
            custom = [line for line in text.splitlines() if line.startswith('command ')]
            names = {re.match(r'command\s+"([^"]+)"', line).group(1) for line in custom}
            current = dest.read_text().splitlines()
            kept = []
            for line in current:
                match = re.match(r'command\s+"([^"]+)"', line)
                if not match or match.group(1) not in names:
                    kept.append(line)
            text = '\n'.join(kept).rstrip() + '\n\n' + '\n'.join(custom) + '\n'
        write(dest, text, 0o700 if src.suffix in {'.sh', '.zsh', '.py'} else 0o600)

    # Merge only known agterm hooks; preserve policies, other hooks and trust hashes.
    hooks = settings.setdefault('hooks', {})
    wanted = json.loads(render((ROOT / 'config/claude-hooks.json').read_text(), home))
    for event, groups in wanted.items():
        existing = {h.get('command') for g in hooks.get(event, []) for h in g.get('hooks', [])}
        for group in groups:
            new = [h for h in group['hooks'] if h.get('command') not in existing]
            if new:
                hooks.setdefault(event, []).append(dict(group, hooks=new))
                existing.update(h.get('command') for h in new)
    settings['statusLine'] = {'type': 'command', 'command': 'sh ' + json.dumps(str(home / '.claude/statusline-command.sh'))}
    write(claude, json.dumps(settings, ensure_ascii=False, indent=2) + '\n', 0o600)
    actions = {'SessionStart': 'session-start', 'UserPromptSubmit': 'user-prompt-submit', 'PreToolUse': 'pre-tool-use', 'PostToolUse': 'post-tool-use', 'PermissionRequest': 'permission-request', 'Stop': 'stop'}
    codex_text = set_feature(set_feature(codex_text, 'hooks', True), 'daemon_auto_start', False)
    config = tomllib.loads(codex_text)
    for event, action in actions.items():
        command = "'%s/.config/agterm/agent-status/agterm-codex-status.sh' %s" % (home, action)
        existing = {h.get('command') for group in config.get('hooks', {}).get(event, []) for h in group.get('hooks', [])}
        if command not in existing:
            codex_text += '\n[[hooks.%s]]\n[[hooks.%s.hooks]]\ntype = "command"\ncommand = %s\n' % (event, event, json.dumps(command))
    tomllib.loads(codex_text)
    write(codex, codex_text, 0o600)

    zsh = home / '.zshrc'
    zsh_text = zsh.read_text() if zsh.exists() else ''
    status = (ROOT / 'config/zsh-status.zsh').read_text()
    pattern = r'# >>> agterm agent-status >>>.*?# <<< agterm agent-status <<<'
    block = '# >>> agterm agent-status >>>\n' + status + '# <<< agterm agent-status <<<'
    if re.search(pattern, zsh_text, re.S):
        zsh_text = re.sub(pattern, lambda m: block, zsh_text, flags=re.S)
    else:
        zsh_text += '\n' + block + '\n'
    if '_agterm_codex_title()' not in zsh_text:
        zsh_text += '\n' + (ROOT / 'config/zsh-title.zsh').read_text()
    write(zsh, zsh_text)
    yazi = home / '.config/yazi/keymap.toml'
    yazi_text = yazi.read_text() if yazi.exists() else ''
    if 'plugin agterm-insert-path' not in yazi_text:
        write(yazi, (ROOT / 'config/yazi-keymap.toml').read_text() + '\n' + yazi_text)
    if ui_settings:
        write(home / 'Library/Application Support/agterm/settings.json', (ROOT / 'config/agterm-settings.json').read_text(), 0o600)
    subprocess.run([sys.executable, str(ROOT / 'activity/install.py'), '--home', str(home)], check=True)
    print('Restored agterm setup to:', home)
    print('Backup:', backup)
    print('Review new agent hooks through /hooks. Reload agterm keymap/config; restart shells for zsh changes.')
    print('No running agent, daemon or terminal was stopped.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home(), help='restore into another home for a rehearsal')
    parser.add_argument('--ui-settings', action='store_true', help='also replace saved agterm appearance/preferences; quit agterm first')
    args = parser.parse_args()
    restore(args.home, args.ui_settings)
