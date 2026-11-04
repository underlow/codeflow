# agterm automatic activity line

`activity.py` is a silent command hook shared by Codex and Claude Code. It derives
a short Russian activity line from the tool name and arguments and sends it to
`agtermctl session info`. It does not call a model, type into a terminal, change
permission decisions, or replace agterm's status hooks.

Examples: `Читаю · Auth.kt`, `Редактирую · Auth.kt`, `Ищу в коде`,
`Тесты · :app:test`, `git diff`, `Думаю`, `Готово`.
Computer-control calls (`mcp__cua_repl.js`, including the flattened MCP name
inside code-mode calls, and `computer`/`computer_use`) show `Computer Use` in red
using agterm's inline markdown. This activity takes precedence over other pending
tools until its result arrives; the next ordinary update restores plain text.
It marks the tool invocation, including any approval delay, rather than claiming
that a human permission prompt is open. It does not detect browser or OS dialogs.
Shell commands are parsed, never executed by the classifier; command arguments,
HTTP headers, prompt text and tool responses are not copied into the sidebar.

Parallel tools and split panes share a locked row state in the user's temporary
directory. A finished tool cannot clear another pending tool. Subagent events
and Codex memory-consolidation transcripts are ignored.
Nested CLI agents launched through scripts (including ephemeral `codex exec`)
are also ignored: the hook checks process ancestry by executable name, so they
cannot overwrite the interactive parent's row through inherited agterm variables.
If process inspection is unavailable, the existing transcript filters still apply.
Lines expire after ten
minutes without an update, including long-running tools; the hook needs no
polling process. Stop means the answer is ready, not that the task succeeded.
Codex PermissionRequest is not treated as a human prompt because Auto Review
can handle it automatically. Claude's actual permission_prompt notification is
displayed as `Жду подтверждения`.

## Install

```sh
/usr/bin/python3 install.py
```

Installs `~/.local/bin/agterm-activity.py`, adds dedicated hooks to
`~/.codex/config.toml` and `~/.claude/settings.json`, and saves private backups in
`~/.config/agterm/activity-backups/`. Existing hooks and trusted hashes are kept.
Run Codex `/hooks` to review/trust the new hooks. Restart/resume the CLI if its
current configuration snapshot does not include them. Claude may also require
review/reload through `/hooks` or a new session. Existing agterm routing through
`AGTERM_SESSION_ID` and `AGTERM_SOCKET` is required; a shared agent daemon that
inherited some other pane's environment cannot be routed correctly by this hook.

```sh
/usr/bin/python3 install.py --uninstall
```

Removes only this hook's configuration, preserving subsequent unrelated edits.
The installed script and backups are retained for inspection.

## Verification

```sh
python3.14 -m unittest discover -s . -v
```

Tests cover code-mode input and the heredoc regression, stale turn results,
subagent filtering, silent subprocess execution, exact targeting, and preservation
of existing configuration during install/uninstall. They do not verify concurrent
processes, real agent-hook delivery, or full restoration on another Mac.
The installer test uses Python 3.11+ for the stdlib TOML parser; the hook itself
runs with macOS `/usr/bin/python3` (3.9+).

`watch_session.py TRANSCRIPT` is a temporary bridge for testing a **currently
running Codex session**, before it can reload/trust new hooks. It follows only
new transcript records and feeds actual tool calls/results into the same hook.
It handles Codex code-mode calls, including nested shell commands. The bridge
uses Codex's internal transcript format, which can change. Do not run it for a
session also running the native activity hooks. Stop its process after testing.

Live acceptance: use real tools in the target session and inspect its `info` in
`agtermctl tree --json`. A successful fixture invocation alone is not live proof.
