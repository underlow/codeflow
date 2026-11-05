#!/usr/bin/env python3
"""Silent, advisory Codex/Claude command hook for agterm's session info line.

Only the stdlib is used. No model calls, terminal scraping, command evaluation,
stdout, permission decisions or changes to the agent's status glyph.
"""
import ast
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata


def clean(value, limit=90):
    text = " ".join("".join(c if not unicodedata.category(c).startswith("C") else " "
                            for c in str(value)).split())
    if len(text) <= limit and len(text.encode("utf-8")) <= 512:
        return text
    # agterm's limit is 512 UTF-8 bytes, including the truncation marker.
    # A byte slice may end inside a character: discard only that incomplete tail.
    prefix = text[:limit - 1].encode("utf-8")[:512 - len("…".encode("utf-8"))]
    return prefix.decode("utf-8", errors="ignore") + "…"


def filename(path):
    return clean(str(path).rstrip("/").split("/")[-1], 55)


def detail(label, value):
    return label + (" · " + clean(value, 65) if value else "")


def shell_activity(command):
    """Describe executable positions, never evaluate code or print full argv."""
    # Heredoc bodies are data/program text, not additional shell commands.
    lines, delimiter = [], None
    for line in command.splitlines():
        if delimiter is not None:
            if line.strip() == delimiter:
                delimiter = None
            continue
        lines.append(line)
        match = re.search(r"<<-?\s*['\"]?([A-Za-z_][A-Za-z_0-9]*)['\"]?", line)
        if match:
            delimiter = match.group(1)
    command = "\n".join(lines)
    try:
        lex = shlex.shlex(command, posix=True, punctuation_chars=";&|()\n")
        lex.whitespace_split = True
        tokens = list(lex)
    except ValueError:
        return "Выполняю команду"
    segments, segment = [], []
    for token in tokens + [";"]:
        if token and all(c in ";&|()\n" for c in token):
            if segment:
                segments.append(segment)
            segment = []
        else:
            segment.append(token)
    labels = []
    for args in segments:
        while args and (re.match(r"^[A-Za-z_][A-Za-z_0-9]*=", args[0]) or args[0] in {"env", "command"}):
            args = args[1:]
        if not args:
            continue
        exe = args[0].split("/")[-1]
        if re.fullmatch(r"python(?:\d+(?:\.\d+)*)?", exe):
            exe = "python3"
        rest = args[1:]
        if exe in {"cd", "echo", "printf", "true"}:
            continue
        if exe in {"bash", "sh", "zsh"} and "-c" in rest:
            pos = rest.index("-c")
            if pos + 1 < len(rest):
                labels.append(shell_activity(rest[pos + 1]))
                continue
        if exe in {"pytest", "py.test", "jest", "vitest"}:
            label = detail("Тесты", exe)
        elif exe in {"gradlew", "gradle", "swift", "cargo", "npm", "pnpm", "yarn", "flutter", "dart", "xcodebuild", "make", "python", "python3"}:
            test = next((a for a in rest if re.search(r"(^|:)test|unittest|pytest|vitest|jest", a, re.I) and not a.startswith("-")), None)
            build = next((a for a in rest if re.search(r"(^|:)(build|assemble|compile)|^check$", a, re.I) and not a.startswith("-")), None)
            lint = next((a for a in rest if re.search(r"(^|:)(lint|detekt)|^fmt$", a, re.I)), None)
            if test:
                label = detail("Тесты", test)
            elif build:
                label = detail("Build", build)
            elif lint:
                label = detail("Lint", lint)
            else:
                script = next((a for a in rest if a.endswith((".py", ".sh"))), "")
                label = detail("Выполняю", filename(script) if script else exe)
        elif exe in {"rg", "grep", "egrep", "fgrep"}:
            label = "Ищу в коде"
        elif exe in {"find", "fd", "ls"}:
            label = "Ищу файлы"
        elif exe in {"cat", "head", "tail", "sed", "bat", "less"}:
            paths = [a for a in rest if not a.startswith("-") and re.search(r"[/]|\.[a-zA-Z0-9]+$", a)]
            label = detail("Читаю", filename(paths[-1])) if paths else "Читаю много файлов"
        elif exe == "git":
            verb = next((a for a in rest if a in {"diff", "status", "log", "show", "commit", "push", "fetch", "pull", "add", "checkout", "switch"}), "")
            label = {"diff": "git diff", "status": "git status", "log": "git log", "show": "git show"}.get(verb, detail("Git", verb))
        elif exe == "curl":
            label = "curl"
        elif exe == "ssh":
            label = "ssh"
        elif exe == "agtermctl":
            label = "agterm"
        else:
            label = detail("Выполняю", exe)
        labels.append(label)
    labels = list(dict.fromkeys(labels))
    return clean(" / ".join(labels[:2])) if labels else "Выполняю команду"


def computer_tool(name):
    # Match tool namespaces, not mentions of computer use in arbitrary arguments.
    return bool(re.fullmatch(r"(?:mcp__)?cua_repl(?:__|\.)[A-Za-z0-9_]+", name)) or name in {
        "computer", "computer_use", "computer.use",
    }


def has_computer_activity(text):
    return "Computer Use" in text.split(" / ")


def tool_activity(name, data):
    if computer_tool(name):
        return "Computer Use"
    short = name.split(".")[-1]
    data = data if isinstance(data, dict) else {"code" if short in {"exec", "js_repl"} else "command": data}
    if short in {"exec", "js_repl"} and "code" not in data and isinstance(data.get("input"), str):
        data = dict(data, code=data["input"])
    lower = name.lower()
    if short in {"Bash", "exec_command", "shell_command", "shell"}:
        description = data.get("description")
        if isinstance(description, str) and clean(description):
            return clean(description)
        cmd = data.get("command", data.get("cmd", ""))
        if isinstance(cmd, list):
            cmd = shlex.join(cmd)
        return shell_activity(str(cmd))
    if short in {"Read", "read_file"} or lower.endswith("__read_file"):
        return detail("Читаю", filename(data.get("file_path", data.get("path", "файл"))))
    if short in {"Edit", "Write", "MultiEdit", "NotebookEdit"}:
        return detail("Редактирую", filename(data.get("file_path", data.get("notebook_path", "файл"))))
    if "apply_patch" in lower:
        patch = data.get("command", data.get("patch", data.get("input", "")))
        paths = re.findall(r"^\*\*\* (?:Update|Add|Delete) File: (.+)$", str(patch), re.M)
        files = list(dict.fromkeys(filename(p) for p in paths))
        return detail("Редактирую", ", ".join(files[:2]) + (" …" if len(files) > 2 else ""))
    if short in {"Grep", "Glob"}:
        return "Ищу в коде" if short == "Grep" else "Ищу файлы"
    if short in {"WebSearch", "WebFetch"} or "web__" in lower or "search_service_web" in lower:
        return "Гуглю" if data.get("search_query") or short == "WebSearch" else "Читаю веб"
    if short in {"Agent", "Task", "spawn_agent"}:
        return "Зову коллегу"
    if short in {"AskUserQuestion", "request_user_input", "request_user_input_async"}:
        return "Жду ответа"
    if short in {"exec", "js_repl"} and isinstance(data.get("code"), str):
        # Codex code-mode: extract string literals passed to nested calls. Never eval JS.
        code = data["code"]
        nested = re.findall(r"tools\.([A-Za-z0-9_]+)\s*\(", code)
        if any(computer_tool(n) for n in nested):
            return "Computer Use"
        quoted = r'''("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')'''
        labels = []
        for match in re.finditer(r'(?:"?(?:cmd|command)"?)\s*:\s*' + quoted, code):
            try:
                labels.append(shell_activity(ast.literal_eval(match.group(1))))
            except (ValueError, SyntaxError):
                pass
        if "apply_patch(" in code:
            labels.append("Редактирую файлы")
        if "web__run(" in code or "search_service_web_run(" in code:
            labels.append("Гуглю" if "search_query" in code else "Читаю веб")
        if not labels:
            nested = re.findall(r"tools\.([A-Za-z0-9_]+)\(", code)
            labels = [tool_activity(n, {}) for n in nested if n not in {"exec", "js_repl"}]
        return clean(" / ".join(dict.fromkeys(labels))) if labels else "Выполняю"
    if short == "write_stdin":
        return "Жду команду"
    if short in {"view_image", "screenshot"}:
        return "Смотрю картинку"
    return detail("Инструмент", name.split("__")[-1])


def nested_agent(processes, pid):
    """Detect CLI agents launched by another CLI agent, through shells/scripts."""
    parents = {}
    for line in processes.splitlines():
        fields = line.strip().split(None, 2)
        if len(fields) == 3 and fields[0].isdigit() and fields[1].isdigit():
            parents[int(fields[0])] = (int(fields[1]), Path(fields[2]).name)
    seen, agents = set(), 0
    while pid in parents and pid not in seen:
        seen.add(pid)
        pid, command = parents[pid]
        if command in {"codex", "claude"}:
            agents += 1
            if agents > 1:
                return True
    return False


def owned_event(payload):
    # Native ephemeral Codex hooks explicitly have no transcript. Process
    # inspection can be denied inside their sandbox, so reject them first.
    if "transcript_path" in payload and payload["transcript_path"] is None:
        return False
    if payload.get("agent_id"):
        return False
    transcript = payload.get("transcript_path")
    if transcript and "/subagents/" in transcript:
        return False
    # Codex internal memory consolidation and forked workers must not repaint the parent.
    if transcript:
        try:
            with open(transcript) as stream:
                first = json.loads(stream.readline(32768))
            if first.get("type") == "session_meta":
                source = first.get("payload", {}).get("source")
                if isinstance(source, dict) and "subagent" in source:
                    return False
        except (OSError, ValueError):
            pass
    # Batch scripts may launch independent `codex exec --ephemeral` processes.
    # They inherit the pane address but have neither a subagent marker nor a
    # transcript. Their lifecycle must not replace the interactive parent's row.
    try:
        processes = subprocess.check_output(
            ["/bin/ps", "-axo", "pid=,ppid=,comm="], text=True,
            stderr=subprocess.DEVNULL, timeout=1)
        if nested_agent(processes, os.getpid()):
            return False
    except (OSError, subprocess.SubprocessError):
        pass
    return True


def background_updates(row):
    """Extract task IDs only; never retain command output or assistant prose."""
    result = row.get("toolUseResult", {})
    if isinstance(result, dict) and result.get("backgroundTaskId"):
        yield ("start", str(result["backgroundTaskId"]))
    if isinstance(result, dict):
        if result.get("task_id") and str(result.get("message", "")).startswith("Successfully stopped task:"):
            yield ("end", str(result["task_id"]))
        task = result.get("task", {})
        if isinstance(task, dict) and task.get("task_id") and task.get("status") in {"completed", "failed", "killed", "stopped"}:
            yield ("end", str(task["task_id"]))
    content = row.get("message", {}).get("content", [])
    if isinstance(content, str):
        content = [{"type": "text", "text": content}]
    for item in content if isinstance(content, list) else []:
        if not isinstance(item, dict) or item.get("type") != "text":
            continue
        for notification in re.findall(r"<task-notification>(.*?)</task-notification>", item.get("text", ""), re.S):
            task = re.search(r"<task-id>([^<]+)</task-id>", notification)
            status = re.search(r"<status>(completed|failed|killed|stopped)</status>", notification)
            if task and status:
                yield ("end", task[1])


def read_background_updates(state, pane, payload):
    path = payload.get("transcript_path")
    # Only Claude transcripts use this schema. Codex transcripts remain untouched.
    if not path or "/.claude/" not in path:
        return []
    cursors = state.setdefault("transcripts", {})
    cursor = cursors.get(pane, {})
    updates = []
    try:
        with open(path, "rb") as stream:
            if cursor.get("path") == path and cursor.get("offset", 0) <= os.fstat(stream.fileno()).st_size:
                stream.seek(cursor.get("offset", 0))
            while True:
                offset = stream.tell()
                line = stream.readline()
                if not line or not line.endswith(b"\n"):
                    stream.seek(offset)
                    break
                try:
                    row = json.loads(line)
                    if row.get("type") in {"user", "api-request-blob"}:
                        updates.extend(background_updates(row))
                except (ValueError, TypeError):
                    continue
            cursors[pane] = {"path": path, "offset": stream.tell()}
    except OSError:
        pass
    return updates


def transition(state, payload, pane, now, background=()):
    """Pure reducer; aggregate independent tool calls, background jobs and panes."""
    event = payload.get("hook_event_name")
    if event not in {"SessionStart", "SessionEnd", "UserPromptSubmit", "PreToolUse", "PostToolUse", "PostToolUseFailure", "Stop", "Interrupt", "PreCompact", "Notification"}:
        return None
    panes = state.setdefault("panes", {})
    # Discard abandoned records, but don't confuse a normal long-running tool with completion.
    for key in list(panes):
        if now - panes[key].get("at", 0) > 86400:
            del panes[key]
    current = panes.setdefault(pane, {"tools": {}, "at": now})
    owner = payload.get("session_id", "")
    if current.get("owner") != owner:
        current.clear()
        current.update(owner=owner, tools={}, at=now)
    turn = payload.get("turn_id")
    if turn and event not in {"UserPromptSubmit", "SessionStart"}:
        if current.get("turn") and turn != current["turn"]:
            return None
        current["turn"] = turn
    jobs = current.setdefault("background", {})
    for action, task in background:
        if action == "start":
            jobs[task] = True
        else:
            jobs.pop(task, None)
    if event in {"SessionStart", "UserPromptSubmit"}:
        current.update(tools={}, turn=turn, text="Работаю" if event == "UserPromptSubmit" else "Готов к работе")
    elif event == "PreToolUse":
        key = payload.get("tool_use_id")
        label = tool_activity(payload.get("tool_name", ""), payload.get("tool_input", {}))
        if key:
            current["tools"][key] = {"text": label, "at": now}
        current["text"] = label
    elif event in {"PostToolUse", "PostToolUseFailure"}:
        key = payload.get("tool_use_id")
        if key:
            current["tools"].pop(key, None)
        response = payload.get("tool_response", {})
        if event == "PostToolUse" and isinstance(response, dict) and response.get("backgroundTaskId"):
            jobs[str(response["backgroundTaskId"])] = True
        current["text"] = "Ошибка" if event == "PostToolUseFailure" else "Думаю"
    elif event == "Stop":
        current.update(tools={}, text="Жду скрипт" if jobs else "Готово")
    elif event == "Interrupt":
        current.update(tools={}, text="Что не так?")
    elif event == "SessionEnd":
        panes.pop(pane, None)
    elif event == "PreCompact":
        current["text"] = "Упс, компакт"
    elif event == "Notification":
        if payload.get("notification_type") != "permission_prompt":
            return None
        current["text"] = "Жду подтверждения"
    current["at"] = now
    # A permission request is not necessarily a human prompt (Auto Review may handle it).
    # Only Claude's real permission_prompt notification sets the waiting label.
    pending = [tool for item in panes.values() for tool in item["tools"].values()]
    if pending:
        computer = [t for t in pending if has_computer_activity(t["text"])]
        latest = max(computer or pending, key=lambda t: t["at"])
        # A real prompt in this pane takes precedence over its pending tool.
        waiting = any(p.get("text") == "Жду подтверждения" for p in panes.values())
        text = "Жду подтверждения" if waiting else latest["text"]
        if len(pending) > 1:
            text += " (+%d)" % (len(pending) - 1)
    elif panes:
        text = max(panes.values(), key=lambda p: p["at"])["text"]
    else:
        text = ""
    return clean(text, 130)


def run(payload, env=None):
    env = os.environ if env is None else env
    sid = env.get("AGTERM_SESSION_ID")
    socket = env.get("AGTERM_SOCKET")
    if not sid or not socket or not owned_event(payload):
        return
    pane = env.get("AGTERM_PANE_ID", env.get("AGTERM_PANE", "left"))
    binary = env.get("AGTERMCTL") or "/Applications/agterm.app/Contents/MacOS/agtermctl"
    if not Path(binary).is_file():
        binary = shutil.which("agtermctl")
    if not binary:
        return
    folder = Path(env.get("AGTERM_ACTIVITY_STATE_DIR", tempfile.gettempdir())) / ("agterm-activity-%d" % os.getuid())
    folder.mkdir(mode=0o700, parents=True, exist_ok=True)
    if folder.is_symlink() or folder.stat().st_uid != os.getuid():
        return
    key = hashlib.sha256((socket + "\0" + sid).encode()).hexdigest()[:32]
    path = folder / (key + ".json")
    # Keep the lock until the control write completes, so older events can't overwrite newer ones.
    fd = os.open(str(path), os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "r+") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        try:
            state = json.load(stream)
        except ValueError:
            state = {}
        updates = read_background_updates(state, pane, payload)
        text = transition(state, payload, pane, time.time(), updates)
        if text is None:
            return
        state["last_event"] = payload.get("hook_event_name")
        state["event_count"] = state.get("event_count", 0) + 1
        previous = state.get("shown")
        if previous != text or time.time() - state.get("shown_at", 0) > 30:
            if text.startswith("Computer Use"):
                # Only our fixed label and generated count enter markdown.
                display = '^[%s](color: "red")' % text
                options = [display, "--markdown", "--hide-after", "600"]
            else:
                options = [text, "--hide-after", "600"] if text else ["--clear"]
            args = [binary, "session", "info"] + options
            args += ["--target", sid, "--socket", socket]
            result = subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
            if result.returncode == 0:
                state.update(shown=text, shown_at=time.time())
                state["history"] = (state.get("history", []) + [{"at": time.time(), "text": text}])[-12:]
        stream.seek(0)
        json.dump(state, stream, ensure_ascii=False)
        stream.truncate()


def main():
    try:
        payload = json.load(sys.stdin)
        if isinstance(payload, dict):
            run(payload)
    except Exception:
        # A display hook must never break a tool or contribute text to the model context.
        pass


if __name__ == "__main__":
    main()
