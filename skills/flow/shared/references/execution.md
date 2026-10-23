# Workspace, state, and resume

## Resolve a request

Find the current Git repository and its registered worktrees with
`git worktree list --porcelain`. A path argument may name a plan directory in
any registered worktree, an existing description file, or a project document
followed by a stage ID, such as `docs/projects/app/project.md S12`. An unmatched
argument needs clarification. Without an argument, inspect `docs/plans/` in the
current checkout and every registered worktree for unfinished flow plans. Show the
feature, profile, phase, branch, and absolute worktree path; let the user choose
when more than one exists. Do not treat older CodeFlow engine plans as native
flow plans or rewrite them. Recognize a native plan by its `state.json`, phase,
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

## Optional project integration

Apply this section only when the user supplies a project document or the selected
flow's saved state links it to a project. For standalone work, do not require or
create a project document, ask for a stage ID, or add `project` and `stage` fields.
The mere presence of project documents in a repository does not attach a flow
to one of them.

A project document and stage ID select that stage's reported problem or desired
work, goal, and relevant project context as input to an ordinary flow. If the ID
is missing, let the user select a stage. Check matching flows in the checkout
and registered worktrees, including completed and cancelled ones. Compare the
current stage goal with their contracts or recorded results, not just their IDs.
Resume unfinished work instead of making a duplicate. If the stage is already
complete, show its outcome and ask whether the user wants to inspect it or
explicitly reopen work; do not start another flow merely because none is unfinished.
Keep a terminal flow's history intact. For agreed reopened work, create a new
flow and reference the prior result in its analysis document; project links both
on return. A materially different goal needs a new stage ID agreed in the project
plan before starting. Do not silently restart cancelled work either.
Project may enter flow directly in this conversation; do not require a handoff
file or a new session. Existing description files with `Project:` and `Stage:`
fields can still identify their project and stage; resolve them to the project
document and check that the selection is current.

Read the project's warning about unverified premises. Agreement on a roadmap
does not establish that a reported bug exists, a proposed cause is correct, a
change is necessary, or a dependency is technically required. Verify the selected
stage's premises during flow analysis, including whether required prior results
are actually available in this checkout. Discuss the profile with the user here
and keep this flow's contract, plan, review, and completion independent. In
`state.json`, retain the optional `project` repository-relative path and `stage`
ID so project can find the work later. Do not infer a profile from the roadmap,
silently change its other stages, or automatically start the next stage.

## Plan documents

Keep each plan under `docs/plans/<date>-<slug>/` in its worktree. A plan's durable
content is its agreed contract, plan and optional tasks, a minimal state file,
and a current findings file only when needed. Do not create per-step result
files, passing-review reports, combined reports, attempt logs, saved prompts,
statistics, or execution directories. Use conversation and Git history for
routine progress. A fresh session must rerun a check if its result cannot be
verified from retained evidence; never report an unobserved check as passed.
Commit deliverable documents and code in
focused commits; preserve unrelated changes. Reviewers do not commit.

## Minimal state

The coordinator owns state writes. For a project stage, once the user chooses to
start it and its checkout is settled, create its plan directory and atomically
write an initial `state.json` before substantive investigation. Capture the exact
`base_commit` before flow changes and record `project`, `stage`, and
`phase: analysis`; include `profile` if already chosen, otherwise omit it until
selection. Commit this registration with explicit paths so a new project session
can discover the work even if analysis is interrupted. This registers started
work; it does not mark analysis complete or require an implementation plan.

After a durable phase or task completes, update `<plan>/state.json` with the
selected `profile`, current `phase`, and exact `base_commit` captured before
flow changes. Add `task` only for an active task and `status` only for paused,
blocked, complete, or cancelled work. Record a reviewed commit when needed to
know whether later code has invalidated a clean review. Derive worktree and
branch from Git, not duplicated state. Write state atomically after the work it
records exists; do not mark an unfinished discussion as complete. The state
file is local coordination data, not a second source of product decisions.
For a project stage, carry `project` and `stage` through later state updates.
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
  "base_commit": "<original Git SHA>",
  "status": "paused"
}
```

Clear `paused` when continuing. The plan and Git history, not an accumulated
attempt counter, show what work remains.

Before marking a flow complete, retain a concise outcome in its existing
`plan.md` or analysis document. State what was delivered or why no change was
warranted, link the relevant artifacts and implementation commits when present,
and summarize actual verification, material limits, and any implication for
dependent stages. Do not keep the only account in the final chat message or
create a separate outcome report. Write completion state only after the outcome
and required work exist, and commit the outcome and state with explicit paths.
For a project stage, the coordinator of flow records execution and results;
project refreshes its document on return. Flow need not edit the project's
status overview.

Put current unresolved findings, evidence, and any user-accepted dispositions
in `<plan>/findings.md` only when there is something to preserve across a
session. Keep references to original agent messages when available. Update or
remove resolved findings when their status changes; do not grow a sequence of
round-numbered files. Keep agreement and acceptance examples in the contract,
not in state or findings.

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
