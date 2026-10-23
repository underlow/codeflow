---
name: delegate-to-codex
description: Delegate implementation or review to Codex and verify its result. Use for "delegate to codex", "отдай разработку codex", "делегируй codex", or /delegate-to-codex.
argument-hint: "[task or review scope, optionally model]"
---

Use the model named by the user; otherwise ask before starting.
For review, pass `--task review`; for changes, pass `--task develop`.

Give Codex a self-contained assignment: desired result, files/diff to inspect,
user decisions, scope, existing work to preserve, and completion checks.

```sh
<skill-dir>/scripts/collab.sh start --task <develop|review> --model <model> [--effort <effort>] <project-root> <<'EOF'
<assignment>
EOF
```

Pass effort only when specified. If model resolution fails, show the returned
choices and ask; do not substitute a model.

Remember the returned terminal ID and `SEND`/`CLOSE` commands. Replace `MESSAGE`
in `SEND` with shell-quoted text prefixed `[claude]` to send corrections or user
updates. Work outside Codex's assigned files or end your turn; do not poll.

Verify the actual changes/checks or review evidence. Send concrete corrections
and inspect the next result. Report meaningful results and unresolved decisions
to the user; do not relay routine progress or repeat the entire assignment.
A blocker leaves the task open. Changing review to development needs the user's
authorization and a new launch.

After accepting the result, run `CLOSE` unless the user asked to keep the session.
For Claude-to-Claude messages use the built-in SendMessage.
