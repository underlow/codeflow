# Machine-readable flow and project progress for a terminal panel
Type: feature | Status: open

## Situation and purpose
While a `flow` runs, the user wants to watch progress in a separate terminal
panel: which steps of the current flow are done, which is running, and which
remain. When the flow belongs to a `project` stage, the panel should also show
where the whole project stands (which stages are done, which one is active).
Today `docs/plans/<plan>/state.json` holds only the current phase and is read
by the coordinator model, so code cannot show a step list from it.

## Agreed behavior and boundaries
- A minimal script (working name `progress.py`) maintains the progress file; the
  coordinator calls its commands instead of editing the file by hand. No extras.
- Only the coordinator writes progress. Subagents (developers, reviewers) do not
  report intermediate activity; the user decided this has no value.
- Storage stays JSON: PyYAML is not in the Python standard library, and with a
  script the format does not matter to the coordinator.
- Must cover the project level, not only one flow. Decided to treat this as a
  separate, larger task rather than part of the flow-text cleanup.
- Per-step model settings were proposed and rejected; do not add them.

## Starting points and open questions
- Flow state rules: `skills/flow/shared/references/execution.md` (section State)
  and `skills/flow/shared/references/project-stage.md`.
- Project skill: `skills/underlow/project/shared/references/project.md`; it finds
  flows by reading `state.json` in `docs/plans/` of every worktree.
- Proposal discussed (not agreed): `init <plan-dir> --feature --profile --base`,
  `add <plan-dir> <step> <title>` for plan tasks, `start|done|skip <plan-dir>
  <step>`, `set <plan-dir> status <value>`, `show <plan-dir>`. Steps of the
  profile would be created by `init`.
- Open: how project-level progress is stored and aggregated; what the panel is
  (existing agterm overlay or something new); whether hooks such as Claude Code
  `SubagentStart`/`SubagentStop` are needed because models forget to call the
  script; whether the script replaces `state.json` entirely.

## Completion check
During a running flow linked to a project stage, a panel shows the project's
stages with the active one marked and the flow's steps with their statuses, and
it updates as the coordinator completes steps without manual edits to JSON.

## Why deferred
During the flow skill cleanup on 2026-10-24 the user judged project-level
progress to be a large separate task and asked to put it in the backlog.

On 2026-10-24 the item was reviewed again and put on hold by the user after a
proof of concept. Findings:
- Project documents (`project.md`) and plans (`plan-medium.md` etc.) have no
  fixed format for stages, statuses, or task IDs, so code cannot parse them
  reliably. Making them parseable needs either a strict Markdown format or
  separate JSON next to the Markdown.
- The proof of concept was a read-only script that scanned `state.json` in
  every worktree and drew the fixed five phases plus the current `task`, grouped by
  `project`/`stage`. It needed no changes to flow. It could not show
  unstarted stages or the task list. The user rejected this result ("нет,
  нафиг"); the script was not added to the repository.
