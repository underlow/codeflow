import contextlib
import io
import json
from pathlib import Path
import tempfile
import tomllib
import unittest

import restore


class RestoreTests(unittest.TestCase):
    def test_existing_policies_hooks_trust_and_unrelated_bindings_survive(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            codex = home / '.codex/config.toml'
            claude = home / '.claude/settings.json'
            keymap = home / '.config/agterm/keymap.conf'
            for path in (codex, claude, keymap):
                path.parent.mkdir(parents=True, exist_ok=True)
            codex.write_text('[features]\nother = true\n[hooks.state.keep]\ntrusted_hash = "keep"\n[[hooks.PreToolUse]]\n[[hooks.PreToolUse.hooks]]\ntype = "command"\ncommand = "policy"\n')
            claude.write_text(json.dumps({'permissions': {'deny': ['Read(secret)']}, 'hooks': {'PreToolUse': [{'hooks': [{'type': 'command', 'command': 'policy'}]}]}}))
            keymap.write_text('command "My command" echo keep\ncommand "Yazi" old\n')
            (home / '.zshrc').write_text('export KEEP=value\n')
            with contextlib.redirect_stdout(io.StringIO()):
                restore.restore(home, ui_settings=True)
            cfg = tomllib.loads(codex.read_text())
            self.assertEqual(cfg['hooks']['state']['keep']['trusted_hash'], 'keep')
            self.assertTrue(cfg['features']['other'])
            self.assertEqual(cfg['hooks']['PreToolUse'][0]['hooks'][0]['command'], 'policy')
            self.assertEqual(json.loads(claude.read_text())['permissions'], {'deny': ['Read(secret)']})
            self.assertIn('command "My command" echo keep', keymap.read_text())
            self.assertNotIn('command "Yazi" old', keymap.read_text())
            self.assertIn('export KEEP=value', (home / '.zshrc').read_text())
            self.assertTrue((home / 'Library/Application Support/agterm/settings.json').exists())
            backups = list((home / '.config/agterm/codeflow-backups').glob('*/.codex/config.toml'))
            self.assertEqual(len(backups), 1)
            self.assertIn('command = "policy"', backups[0].read_text())


if __name__ == '__main__':
    unittest.main()
