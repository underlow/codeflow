#!/usr/bin/env python3
"""Install/remove only this hook, preserving unrelated configuration and trust."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import shlex
import stat
import tempfile

EVENTS = ["SessionStart", "UserPromptSubmit", "PreToolUse", "PostToolUse", "Stop", "PreCompact"]
START = "# >>> agterm-activity >>>"
END = "# <<< agterm-activity <<<"


def replace_file(path, content, default_mode=0o600):
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else default_mode
    fd, tmp = tempfile.mkstemp(prefix=".agterm-activity-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w") as stream:
            stream.write(content)
        os.chmod(tmp, mode)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def install(home, uninstall=False):
    destination = home / ".local/bin/agterm-activity.py"
    command = "/usr/bin/python3 " + shlex.quote(str(destination))
    codex = home / ".codex/config.toml"
    claude = home / ".claude/settings.json"
    toml = codex.read_text() if codex.exists() else ""
    if START in toml:
        start = toml.index(START)
        end = toml.index(END, start) + len(END)
        toml = toml[:start].rstrip() + "\n" + toml[end:].lstrip("\n")
    if not uninstall:
        block = [START]
        for event in EVENTS + ["Interrupt", "SessionEnd"]:
            block += ["[[hooks.%s]]" % event, "[[hooks.%s.hooks]]" % event,
                      'type = "command"', "command = " + json.dumps(command), "timeout = 3", ""]
        block.append(END)
        toml = toml.rstrip() + "\n\n" + "\n".join(block) + "\n"
    settings = json.loads(claude.read_text()) if claude.exists() else {}
    hooks = settings.setdefault("hooks", {})
    for event in list(hooks):
        groups = []
        for group in hooks[event]:
            group = dict(group)
            group["hooks"] = [h for h in group.get("hooks", []) if h.get("command") != command]
            if group["hooks"]:
                groups.append(group)
        if groups:
            hooks[event] = groups
        else:
            del hooks[event]
    if not uninstall:
        for event in EVENTS + ["PostToolUseFailure", "SessionEnd", "Notification"]:
            group = {"hooks": [{"type": "command", "command": command, "timeout": 3}]}
            if event == "Notification":
                group["matcher"] = "permission_prompt"
            hooks.setdefault(event, []).append(group)
    backup = home / ".config/agterm/activity-backups" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup.mkdir(parents=True, mode=0o700)
    for path, name in ((codex, "codex-config.toml"), (claude, "claude-settings.json")):
        if path.exists():
            shutil.copy2(path, backup / name)
            os.chmod(backup / name, 0o600)
    if not uninstall:
        replace_file(destination, Path(__file__).with_name("activity.py").read_text(), 0o700)
    replace_file(codex, toml)
    replace_file(claude, json.dumps(settings, ensure_ascii=False, indent=2) + "\n")
    print(("Removed" if uninstall else "Installed") + " agterm activity hooks for Codex and Claude Code")
    print("Backup: " + str(backup))
    if not uninstall:
        print("Codex: open /hooks and trust the new agterm-activity hooks; existing trust was not changed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--uninstall", action="store_true")
    args = parser.parse_args()
    install(args.home, args.uninstall)
