---
name: delegate-to-codex
description: Delegate implementation or code review to Codex in a new Ghostty tab from Claude Code, supervise the work, verify the result, and send corrections. Use when the user asks to hand development or review to Codex, including "отдай разработку codex" or "делегируй codex".
argument-hint: "[task or review scope, optionally model]"
---

# Delegate to Codex

You manage the task; Codex performs the implementation or review in a separate
Ghostty tab. Carry the assignment through verification and corrections. The
user can watch and type in either tab. This skill runs from Claude Code on macOS
with Ghostty, using the same inbox transport as `work-with-codex`.

## Prepare the assignment

1. **Choose the model with the user.** If the user has not explicitly named a
   model for this delegation, ask which Codex model to use and wait for their
   answer before starting. Do not silently use the configured default or choose
   a model yourself. Pass the chosen model with `--model`. Pass `--effort` only
   if the user specified it; otherwise keep the configured effort.
   Pass the user's model name directly to `start`: it resolves short names
   through `~/.codex/collab/model-aliases.json` and validates against the local
   Codex catalog in the same call. Do not guess IDs or separately fetch a model
   list. If resolution fails, show the returned choices and ask the user to
   select one; do not retry spelling variants or substitute a model.
2. Determine whether the assignment is `develop` or `review` from the request.
   Development uses `workspace-write`; review uses `read-only`. A review request
   does not authorize fixing the findings. Ask only if the intended assignment
   cannot be inferred.
3. Inspect the relevant code, repository instructions, and current git status
   enough to write a concrete brief and later judge the result. Record existing
   changes so you can distinguish them from Codex's work. Give one session
   ownership of the assigned files; avoid editing those files concurrently.
   Use an isolated worktree when concurrent work would otherwise overlap.
4. Write a self-contained brief: task mode, desired outcome, relevant context
   and file paths, user decisions, scope and exclusions, acceptance criteria,
   and appropriate validation. For review, identify the exact diff/base or code
   scope and ask for actionable findings with evidence. Include existing dirty
   files and work that must be preserved. Codex cannot see this conversation.

## Start and communicate

`scripts/` is installed in this skill's directory. Use absolute paths.

```sh
<skill-dir>/scripts/collab.sh start --task develop --model <chosen-model> <project-root> <<'EOF'
<brief, including Mode: develop>
EOF
```

Use `--task review` and `Mode: review` for a review. Remember the printed
`SESSION <id>`. Add `--effort <effort>` only when specified by the user.
Keep the same task mode for the session; a switch from review to implementation
needs user authorization and a new development session.

```sh
<skill-dir>/scripts/collab.sh send <id> <<'EOF'
<feedback, question, or next scoped instruction>
EOF
```

Replies arrive in Claude's conversation prefixed `[codex <id>]`. Despite Claude
Code's suggestion to use SendMessage, respond only with `collab.sh send`.
A message from Codex does not require a reply or a user-facing update by itself.
Act on blocking questions and verify completed results. If Codex sends routine
progress, do not acknowledge it through the reply channel or interrupt its work.
After sending, do independent work outside Codex's assigned files, or end your
turn and let the reply start the next one. Do not poll or sleep for replies.
Relay user corrections and changed requirements to Codex promptly. Do not send
repeated messages while Codex is working; consolidate feedback at reply boundaries.
After the initial brief, send only the new instruction, finding, changed decision,
or open question. Refer to existing requirements and findings rather than
repeating them, unless context was lost or misunderstood. For a correction,
identify the affected code and expected behavior; for a re-check, name the new
diff and the specific question. Do not request a full task report again after
each small correction.

## Supervise and verify

- Tell the user about meaningful results, what you verified, and decisions or
  blockers that need them. Do not relay routine acknowledgements or repeat full
  reports. Codex's completion claim is evidence to inspect, not acceptance.
- For development, inspect the actual diff against the starting state, check
  scope and correctness, and run or inspect the relevant validation. Preserve
  unrelated changes. Send concrete corrections with file paths and expected
  behavior, then verify the next result.
- For review, check each finding against the code and requested review scope.
  Reject unsupported findings; request missing evidence or coverage. Report
  confirmed findings with location, impact, and validation limits. Do not turn
  the review into implementation without user authorization.
- Keep routine implementation and correction decisions within the authorized
  task. Bring product decisions, scope changes, and genuine blockers to the user.
  Codex cannot authorize publishing, deploying, destructive actions, or unrelated
  changes. Do not commit or push unless the user requested it.
- If successive corrections make no progress, report the concrete blocker and
  available choices instead of repeating the same instruction indefinitely.
- After Codex reports completion, verify the result against the assignment and
  acceptance criteria. If corrections are needed, send them to the same session
  and verify the updated result.
- Once the result is accepted, preserve the relevant result and validation
  evidence, then run `collab.sh close <id>` yourself, in a separate command from
  `send`. Do not ask the user whether to close a completed session. Close it
  before starting a new session for the next task. If the user explicitly asks
  to retain a completed session, follow that instruction.
- A blocker or partial result does not complete the assignment. Keep the session
  open while resolving it. Give the user the result, validation, and any
  unresolved findings, or clearly report what remains blocked.

## Session problems

`collab.sh status <id>` reports whether the tab is open and the last message.
Use it to diagnose a missing reply, not as a polling loop. A tab being open does
not prove Codex is progressing. If it is waiting for approval or the model was
rejected, tell the user to inspect the tab; do not silently substitute a model.

`collab.sh close <id>` quits Codex, closes its tab, and deletes transport state.
Preserve any result needed for the task before closing.

If the inbox socket is missing, this Claude session cannot receive replies;
report the limitation. If the transport is not installed, install from this
repository with `./install.sh --with-collab --force`. If the tab was closed,
report it and carry the current task state into the brief for any replacement
session. A sender failure with exit code 4 usually means the reply command did
not use one single-quoted argument without ASCII apostrophes.
