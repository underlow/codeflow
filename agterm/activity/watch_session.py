#!/usr/bin/env python3
"""Temporary live-session test bridge: actual transcript events -> the same hook.

Use when newly configured lifecycle hooks cannot load into an already running
agent. Reads only appended events. No prompts or agent commands are injected.
"""
import argparse
import importlib
import json
import os
from pathlib import Path
import signal
import time

import activity


def watch(path):
    common = {"session_id": os.environ.get("CODEX_THREAD_ID", str(path)), "transcript_path": str(path)}
    calls = {}
    # A restart of the temporary bridge must not retain unfinished records from its old run.
    activity.run(dict(common, hook_event_name="UserPromptSubmit"))
    with path.open() as stream:
        stream.seek(0, 2)
        while True:
            pos = stream.tell()
            line = stream.readline()
            if not line or not line.endswith("\n"):
                stream.seek(pos)
                time.sleep(0.2)
                continue
            try:
                row = json.loads(line)
            except ValueError:
                continue
            p = row.get("payload", {})
            event = None
            if row.get("type") == "response_item":
                kind, key = p.get("type"), p.get("call_id")
                if kind in {"function_call", "custom_tool_call"}:
                    args = p.get("arguments", p.get("input", {}))
                    if kind == "function_call" and isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except ValueError:
                            pass
                    event = dict(hook_event_name="PreToolUse", tool_name=p.get("name", ""), tool_input=args, tool_use_id=key)
                    calls[key] = event
                elif kind in {"function_call_output", "custom_tool_call_output"}:
                    original = calls.pop(key, None)
                    if original:
                        event = dict(original, hook_event_name="PostToolUse")
            elif row.get("type") == "event_msg":
                if p.get("type") == "task_started":
                    event = {"hook_event_name": "UserPromptSubmit"}
                elif p.get("type") in {"task_complete", "task_completed"}:
                    event = {"hook_event_name": "Stop"}
                elif p.get("type") == "turn_aborted":
                    event = {"hook_event_name": "Interrupt"}
            if event:
                try:
                    importlib.reload(activity)
                    activity.run(dict(common, **event))
                except Exception:
                    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", type=Path)
    args = parser.parse_args()
    watch(args.transcript)
