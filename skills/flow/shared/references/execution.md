# Workspace, state, and resume

## Resolve a request

Find the current Git repository and its registered worktrees with
`git worktree list --porcelain`. A path argument may name a plan directory in
any registered worktree, an existing description file, or a project document
followed by a stage ID, such as `docs/projects/app.md S12`. An unmatched
argument needs clarification. Without an argument, inspect `docs/plans/` in the
current checkout and every registered worktree for unfinished flow plans. Show the
feature, profile, phase, branch, and absolute worktree path; let the user choose
when more than one exists. Recognize a flow plan by its `state.json`, phase,
base commit, and selected profile. A project-stage registration may have no
profile yet; recognize it by its `project`, `stage`, `phase`, and `base_commit`
fields and obtain the profile on resume. A completed or cancelled plan is terminal.

For a new request, understand the feature before choosing a profile. Propose the
profile appropriate to the scope and let the user choose another. Use a
`flow/<slug>` branch in the current checkout by default, adding a suffix if
occupied. If existing user changes would overlap, offer a separate worktree or
let the user resolve them. Never stash, discard, or commit their work as setup.
Honor an explicit workspace choice. In a worktree, pass its absolute path to all
tools and agents; creating one does not change the coordinator session's cwd.

When the user supplies a project document or the selected flow's state links
it to a project, also follow [project-stage.md](project-stage.md). For
standalone work, do not require or create a project document, ask for a stage
ID, or add `project` and `stage` fields. The mere presence of project documents
in a repository does not attach a flow to one of them.

## Plan documents

Keep each plan under `docs/plans/<date>-<slug>/` in its worktree. A plan
directory holds only the agreed contract documents, `plan.md` and optional
`tasks/`, `state.json`, and `findings.md` when needed. Use conversation and Git
history for routine progress. A fresh session must rerun a check if its result
cannot be verified from retained evidence; never report an unobserved check as
passed. Commit deliverable documents and code in focused commits; preserve
unrelated changes. Reviewers do not commit.

## Minimal state

The coordinator owns state writes. After a durable phase or task completes,
update `<plan>/state.json` with the selected `profile`, current `phase`, and
exact `base_commit` captured before flow changes. Add `task` only for an active
task and `status` only for paused, blocked, complete, or cancelled work. Record
a reviewed commit when needed to know whether later code has invalidated a clean
review. Derive worktree and branch from Git, not duplicated state. Write state
atomically after the work it records exists; do not mark an unfinished
discussion as complete. The state file is local coordination data, not a second
source of product decisions.
After the user confirms development agent settings, retain the selected
platform, model, and reasoning effort in a `development_agent` object in
`state.json`, with `platform`, `model`, and `effort` fields. Use the actual
platform and values. Record task-specific exceptions in an optional `tasks`
object keyed by the plan's task ID only when the user chose them. This is a
small resume pointer, not a history of every agent call. If no choice was made
before pausing at the plan boundary, leave it absent and ask before
implementation on resume. When resuming on another platform or after a model
becomes unavailable, reconfirm an applicable choice with the user. If the user
stops after confirming a review plan but before its reviewers start, retain the
pending reviewer choices with their scope and current commit; discard them when
the scope changes or the review starts. Do not add model assignments to the
behavioral contract or plan.
Use `analysis`, `planning`, `implementation`, `review`, or `delivery` as the
active phase. For example, after stopping at the committed plan boundary:

```json
{
  "profile": "medium",
  "phase": "implementation",
  "base_commit": "<Git SHA before flow changes>",
  "status": "paused"
}
```

Clear `paused` when continuing. The plan and Git history show what work remains.

Before marking a flow complete, retain a concise outcome in its existing
`plan.md` or analysis document. State what was delivered or why no change was
warranted, link the relevant artifacts and implementation commits when present,
and summarize actual verification, material limits, and any implication for
dependent stages. Do not keep the only account in the final chat message or
create a separate outcome report. Write completion state only after the outcome
and required work exist, and commit the outcome and state with explicit paths.

Put current unresolved findings, evidence, and any user-accepted dispositions
in `<plan>/findings.md` only when there is something to preserve across a
session. Keep references to original agent messages when available. Update or
remove resolved findings when their status changes; keep one current file.
Keep agreement and acceptance examples in the contract, not in state or findings.

## Resume from the main repository

An invocation in the main checkout must discover unfinished plans inside its
registered worktrees as well as its own. A selected plan's path supplies the
checkout for every subsequent tool and agent. Verify that worktree still exists,
its branch and Git history match the saved base, and the plan files are present.
Read state, contract, plan, findings if any, current diff, and relevant commits.
Determine what actually finished before continuing; a stale state file is not a
reason to repeat valid work or call a draft complete. If an agent may still be
running, account for it before starting another. If the worktree was removed or
never reached its first durable plan file, explain what can be recovered from
Git and conversation. Ask only for information that cannot be inferred.

A new coordinator session resumes at the recorded phase. After a committed plan
and a user's choice to stop, implementation is the next phase; the new session
checks the confirmed development model and effort, or obtains that choice if it
is missing, before starting a fresh developer agent. If work after a clean
review changed the reviewed commit, reassess the affected scope before delivery.
Do not push, merge, delete branches or worktrees, or move plan directories as
routine cleanup.
