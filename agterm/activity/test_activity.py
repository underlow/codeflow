import copy
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import activity
import install


class ActivityTests(unittest.TestCase):
    def test_utf8_limit_with_four_byte_characters(self):
        for text, limit in (("😀" * 200, 130), ("a" * 508 + "😀b", 1000),
                            ("a" * 509 + "😀", 1000)):
            with self.subTest(limit=limit, bytes=len(text.encode("utf-8"))):
                result = activity.clean(text, limit)
                self.assertLessEqual(len(result.encode("utf-8")), 512)
                self.assertLessEqual(len(result), limit)
                self.assertTrue(result.endswith("…"))
                self.assertTrue(text.startswith(result[:-1]))
        self.assertEqual(activity.clean("a" * 512, 1000), "a" * 512)

    def test_code_mode_nested_tools(self):
        code = 'text(await tools.exec_command({cmd:"swift test"}));'
        self.assertEqual(activity.tool_activity("exec", {"code": code}), "Тесты · test")
        code = 'await tools.exec_command({cmd:"rg -n foo src"}); await tools.exec_command({cmd:"git diff"});'
        self.assertEqual(activity.tool_activity("exec", {"code": code}), "Ищу в коде / git diff")
        self.assertEqual(activity.tool_activity("exec", code), "Ищу в коде / git diff")

    def test_heredoc_body_is_not_shell_code(self):
        command = "python3 - <<'PY'\nprint('test')\nkey=hashlib.sha256((sock+'\\0'+sid).encode())\nPY"
        self.assertEqual(activity.shell_activity(command), "Выполняю · python3")

    def event(self, name, key="a", turn="t1", **extra):
        return dict(hook_event_name=name, tool_name="Bash", tool_input={"command": "swift test"},
                    tool_use_id=key, session_id="s1", turn_id=turn, **extra)

    def test_late_result_from_previous_turn_is_ignored(self):
        state = {}
        activity.transition(state, self.event("UserPromptSubmit", turn="t1"), "left", 1)
        activity.transition(state, self.event("UserPromptSubmit", turn="t2"), "left", 2)
        before = copy.deepcopy(state)
        self.assertIsNone(activity.transition(state, self.event("PostToolUse", turn="t1"), "left", 3))
        self.assertEqual(state, before)

    def test_auto_review_is_not_a_human_prompt(self):
        self.assertIsNone(activity.transition({}, self.event("PermissionRequest"), "left", 1))
        state = {}
        activity.transition(state, self.event("PreToolUse"), "left", 1)
        self.assertEqual(activity.transition(state, self.event("Notification", notification_type="permission_prompt"), "left", 2), "Жду подтверждения")
        self.assertEqual(activity.transition(state, self.event("PostToolUse"), "left", 3), "Думаю")

    def test_subagents_and_hidden_memory_are_ignored(self):
        self.assertFalse(activity.owned_event({"agent_id": "worker"}))
        with tempfile.TemporaryDirectory() as tmp:
            transcript = Path(tmp) / "rollout.jsonl"
            transcript.write_text(json.dumps({"type": "session_meta", "payload": {"source": {"subagent": "memory_consolidation"}}}))
            self.assertFalse(activity.owned_event({"transcript_path": str(transcript)}))

    def test_hook_boundary_targets_exact_session_and_stays_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            fake = target / "agtermctl"
            log = target / "argv.json"
            fake.write_text("#!/usr/bin/python3\nimport json,sys\nopen(" + repr(str(log)) + ", 'w').write(json.dumps(sys.argv[1:]))\n")
            fake.chmod(0o700)
            env = dict(os.environ, AGTERM_SESSION_ID="exact-session", AGTERM_PANE_ID="exact-pane", AGTERM_SOCKET="/specific.sock", AGTERMCTL=str(fake), AGTERM_ACTIVITY_STATE_DIR=tmp)
            result = subprocess.run([sys.executable, str(Path(activity.__file__))], input=json.dumps(self.event("PreToolUse")), text=True, capture_output=True, env=env)
            self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))
            args = json.loads(log.read_text())
            self.assertIn("Тесты · test", args)
            self.assertEqual(args[args.index("--target") + 1], "exact-session")
            self.assertEqual(args[args.index("--socket") + 1], "/specific.sock")

    def test_outside_agterm_and_bad_input_are_silent(self):
        env = {k: v for k, v in os.environ.items() if not k.startswith("AGTERM")}
        for data in ("bad json", json.dumps(self.event("PreToolUse"))):
            result = subprocess.run([sys.executable, activity.__file__], input=data, text=True, capture_output=True, env=env)
            self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))


class InstallTests(unittest.TestCase):
    def test_preserves_existing_hooks_and_trust_and_uninstalls_own_hooks(self):
        import tomllib
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            codex = home / ".codex/config.toml"
            claude = home / ".claude/settings.json"
            codex.parent.mkdir()
            claude.parent.mkdir()
            original = '[features]\nhooks = true\n[hooks.state.original]\ntrusted_hash = "keep"\n[[hooks.Stop]]\n[[hooks.Stop.hooks]]\ntype = "command"\ncommand = "existing-stop"\n'
            codex.write_text(original)
            settings = {"model": "keep", "hooks": {"Stop": [{"hooks": [{"type": "command", "command": "existing-stop"}]}]}}
            claude.write_text(json.dumps(settings))
            with contextlib.redirect_stdout(io.StringIO()):
                install.install(home)
                install.install(home)
            config = tomllib.loads(codex.read_text())
            self.assertEqual(config["hooks"]["state"]["original"]["trusted_hash"], "keep")
            self.assertEqual(len(config["hooks"]["Stop"]), 2)
            self.assertEqual(len(config["hooks"]["PreToolUse"]), 1)
            after = json.loads(claude.read_text())
            self.assertEqual(after["model"], "keep")
            self.assertEqual(len(after["hooks"]["Stop"]), 2)
            self.assertEqual(after["hooks"]["Stop"][0], settings["hooks"]["Stop"][0])
            with contextlib.redirect_stdout(io.StringIO()):
                install.install(home, uninstall=True)
            self.assertEqual(tomllib.loads(codex.read_text()), tomllib.loads(original))
            self.assertEqual(json.loads(claude.read_text()), settings)


if __name__ == "__main__":
    unittest.main()
