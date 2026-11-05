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
from unittest.mock import patch

import activity
import install


class ActivityTests(unittest.TestCase):
    def test_shell_description_reaches_activity_line(self):
        event = self.event("PreToolUse")
        event["tool_input"] = {
            "command": "swift test",
            "description": "Export orders for next words of other pairs",
        }
        self.assertEqual(activity.transition({}, event, "left", 1),
                         "Export orders for next words of other pairs")

    def test_shell_description_is_cleaned_and_bounded(self):
        description = "Export\norders\x00 " + "😀" * 200
        label = activity.tool_activity("Bash", {"description": description})
        self.assertTrue(label.startswith("Export orders "))
        self.assertNotIn("\x00", label)
        self.assertNotIn("\n", label)
        self.assertLessEqual(len(label), 90)
        self.assertLessEqual(len(label.encode("utf-8")), 512)

    def test_unusable_shell_description_falls_back_to_command(self):
        for description in (None, "", " \n\x00", 42, {"text": "title"}):
            with self.subTest(description=description):
                self.assertEqual(activity.tool_activity("Bash", {
                    "command": "swift test", "description": description,
                }), "Тесты · test")

    def test_ephemeral_hooks_are_ignored_even_when_ps_is_denied(self):
        with patch.object(activity.subprocess, "check_output", side_effect=PermissionError) as ps:
            for name in ("SessionStart", "UserPromptSubmit", "PreToolUse", "Stop", "SessionEnd"):
                self.assertFalse(activity.owned_event(dict(self.event(name), transcript_path=None)))
            ps.assert_not_called()

    def test_background_wait_survives_intervening_tools_and_turns(self):
        state = {}
        activity.transition(state, self.event("PreToolUse"), "left", 1)
        post = dict(self.event("PostToolUse"), tool_response={"stdout": "", "backgroundTaskId": "job"})
        activity.transition(state, post, "left", 2)
        self.assertEqual(activity.transition(state, self.event("Stop"), "left", 3), "Жду скрипт")
        activity.transition(state, self.event("UserPromptSubmit", turn="t2"), "left", 4)
        activity.transition(state, self.event("PreToolUse", turn="t2"), "left", 5)
        activity.transition(state, self.event("PostToolUse", turn="t2"), "left", 6)
        self.assertEqual(activity.transition(state, self.event("Stop", turn="t2"), "left", 7), "Жду скрипт")
        self.assertEqual(activity.transition(state, self.event("Stop", turn="t2"), "left", 8, [("end", "job")]), "Готово")

    def test_background_transcript_recovery_and_incremental_completion(self):
        with tempfile.TemporaryDirectory() as tmp:
            transcript = Path(tmp) / ".claude/projects/session.jsonl"
            transcript.parent.mkdir(parents=True)
            rows = [
                {"type": "user", "toolUseResult": {"backgroundTaskId": "finished", "stdout": "private"}},
                {"type": "user", "message": {"content": [{"type": "text", "text": '<task-notification><task-id>finished</task-id><status>completed</status></task-notification>'}]}},
                {"type": "user", "toolUseResult": {"backgroundTaskId": "running"}},
                {"type": "user", "toolUseResult": {"backgroundTaskId": "cancelled"}},
                {"type": "user", "toolUseResult": {"task_id": "cancelled", "message": "Successfully stopped task: cancelled"}},
                {"type": "user", "toolUseResult": {"taskId": "monitor"}},
            ]
            transcript.write_text(''.join(json.dumps(row) + '\n' for row in rows))
            state = {}
            event = dict(self.event("Stop"), transcript_path=str(transcript))
            updates = activity.read_background_updates(state, "left", event)
            self.assertEqual(activity.transition(state, event, "left", 1, updates), "Жду скрипт")
            self.assertEqual(state['panes']['left']['background'], {"running": True})
            self.assertEqual(activity.read_background_updates(state, "left", event), [])
            notice = {"type": "user", "message": {"content": '<task-notification><task-id>running</task-id><status>failed</status></task-notification>'}}
            with transcript.open('a') as stream:
                stream.write(json.dumps(notice))
            self.assertEqual(activity.read_background_updates(state, "left", event), [])
            with transcript.open('a') as stream:
                stream.write('\n')
            updates = activity.read_background_updates(state, "left", event)
            self.assertEqual(activity.transition(state, event, "left", 2, updates), "Готово")
            self.assertNotIn('private', json.dumps(state))

    def test_nested_cli_agents_through_batch_script(self):
        processes = '''
1 0 launchd
10 1 /bin/zsh
20 10 claude
30 20 /bin/bash
40 30 /usr/bin/python3
50 40 /opt/homebrew/bin/codex
60 50 /bin/sh
70 60 /usr/bin/python3
80 20 /bin/sh
90 80 /usr/bin/python3
100 10 /opt/homebrew/bin/codex
110 100 /bin/sh
120 110 /usr/bin/python3
'''
        self.assertTrue(activity.nested_agent(processes, 70))
        self.assertFalse(activity.nested_agent(processes, 90))
        self.assertFalse(activity.nested_agent(processes, 120))
        # Missing ancestors and malformed/cyclic records must terminate safely.
        self.assertFalse(activity.nested_agent('1 2 python3\n2 1 sh\nbad', 1))
        with patch.object(activity.subprocess, "check_output", return_value=processes), patch.object(activity.os, "getpid", return_value=70):
            for event in ("SessionStart", "UserPromptSubmit", "PreToolUse", "Stop", "SessionEnd"):
                self.assertFalse(activity.owned_event(self.event(event)))

    def test_nested_cli_event_does_not_touch_row_or_control_channel(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(AGTERM_SESSION_ID="session", AGTERM_SOCKET="/specific.sock",
                       AGTERM_ACTIVITY_STATE_DIR=tmp, AGTERMCTL=sys.executable)
            processes = '1 0 claude\n2 1 python3\n3 2 codex\n4 3 python3'
            with patch.object(activity.subprocess, "check_output", return_value=processes), patch.object(activity.os, "getpid", return_value=4), patch.object(activity.subprocess, "run") as send:
                activity.run(self.event("SessionStart"), env)
                send.assert_not_called()
                self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_computer_tool_names_and_code_mode(self):
        for name in ("mcp__cua_repl.js", "mcp__cua_repl__js", "cua_repl.js", "computer", "computer_use"):
            self.assertEqual(activity.tool_activity(name, {}), "Computer Use")
        code = 'await tools.exec_command({cmd:"git diff"}); await tools.mcp__cua_repl__js({code:"await tab.click()"});'
        self.assertEqual(activity.tool_activity("functions.exec", {"code": code}), "Computer Use")
        self.assertNotEqual(activity.tool_activity("exec_command", {"cmd": "rg computer_use README.md"}), "Computer Use")

    def test_computer_use_has_priority_until_its_result(self):
        state = {}
        cua = self.event("PreToolUse", key="cua")
        cua.update(tool_name="mcp__cua_repl.js", tool_input={"code": "await cua.getState()"})
        self.assertEqual(activity.transition(state, cua, "left", 1), "Computer Use")
        self.assertEqual(activity.transition(state, self.event("PreToolUse"), "right", 2), "Computer Use (+1)")
        self.assertEqual(activity.transition(state, dict(cua, hook_event_name="PostToolUse"), "left", 3), "Тесты · test")
        self.assertEqual(activity.transition(state, self.event("PostToolUse"), "right", 4), "Думаю")

    def test_computer_use_red_and_plain_text_reset_at_control_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(AGTERM_SESSION_ID="session", AGTERM_SOCKET="/specific.sock",
                       AGTERM_ACTIVITY_STATE_DIR=tmp, AGTERMCTL=sys.executable)
            event = self.event("PreToolUse")
            event.update(tool_name="mcp__cua_repl.js", tool_input={})
            with patch.object(activity.subprocess, "run") as send:
                send.return_value.returncode = 0
                activity.run(event, env)
                args = send.call_args.args[0]
                self.assertIn('^[Computer Use](color: "red")', args)
                self.assertIn("--markdown", args)
                activity.run(dict(event, hook_event_name="PostToolUse"), env)
                args = send.call_args.args[0]
                self.assertIn("Думаю", args)
                self.assertNotIn("--markdown", args)

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
