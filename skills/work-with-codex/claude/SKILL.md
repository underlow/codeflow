---
name: work-with-codex
description: Discuss a task with Codex as a peer. Use for "work with codex", "discuss with codex", "brainstorm with codex", or /work-with-codex.
argument-hint: "[topic]"
---

Form your own assessment, then ask Codex for an independent one. Give it the
problem, relevant files, user decisions, and open questions; include your
conclusion only when asking for a critique of it.

```sh
<skill-dir>/scripts/collab.sh start [--model <model>] [--effort <effort>] <project-root> <<'EOF'
<brief>
EOF
```

Pass model/effort only when the user specified them. If model resolution fails,
show the returned choices and ask; do not guess another model.

Remember the returned terminal ID and `SEND`/`CLOSE` commands. To send, replace
`MESSAGE` in `SEND` with shell-quoted text prefixed `[claude]`. Continue your own
work or end your turn to receive the reply; do not poll.

Compare assessments, check material disagreements, and send new findings or
questions. Do not repeat agreements or manufacture another discussion round.
Bring the resulting proposal and unresolved decisions to the user.

Keep Codex open until the user ends the discussion, then run `CLOSE`.
For Claude-to-Claude messages use the built-in SendMessage.
