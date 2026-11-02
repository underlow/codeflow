# Workspace, state, and resume

## Resolve a request

List the repository's worktrees with `git worktree list --porcelain`. An
argument may name a plan directory in any worktree, a description file, or a
project document with a stage ID, such as `docs/projects/app.md S12`; ask about
an argument that matches none. Without an argument, look for unfinished plans in
`docs/plans/` of every worktree and show each one's feature, profile, phase,
branch, and absolute path. A plan is recognized by its `state.txt`, or
`state.json` in older plans. Completed and cancelled plans are terminal. A
backlog item file as the request is the flow's source document.

A new request starts with the problem step from [phases.md](phases.md); do not
ask for a profile before `problem.md` is confirmed. If the work is more than two
weeks for a developer who knows the code, offer to split it into `project`
stages or separate flows. Until the user confirms `problem.md` and either
chooses the profile or agrees that no change is warranted, create no branch,
plan directory, state, or commit; keep experiments outside the repository or
remove them. Then start the work:

1. Choose a `flow/<slug>` branch in the current checkout by default, adding a
   suffix if the name is taken. If the user's uncommitted changes would overlap,
   offer a separate worktree or let them resolve it; never stash, discard, or
   commit their work. Before creating a worktree, tell the user if the analysis
   relied on uncommitted changes it will not contain.
2. For a backlog item, move it into the plan directory as `backlog-item.md` and
   commit only that move on the current branch, so other checkouts stop
   offering it.
3. Create the branch or worktree, write the document and `state.txt`, and
   commit them. Record the item's original path and the branch from step 2 in
   the `backlog` line.

In a worktree, pass its absolute path to every tool and agent.

When the user supplies a project document or the plan's state names a project,
also follow [project-stage.md](project-stage.md). Otherwise ignore project
documents.

## Plan directory

Each plan lives in `docs/plans/<date>-<slug>/` and holds only the contract
documents, `plan.md` with optional `tasks/`, `state.txt`, `backlog-item.md`
when taken from the backlog, and `findings.md` when needed. Routine progress
lives in the conversation and Git history.

Besides the backlog item move, commit only at these points, always with explicit
paths: the first contract document with the initial state; the remaining
contract documents and the plan together once planning is finished; each
developer's completed task; and the outcome with the completion state.

## State

You alone write `state.txt`, after the work it records exists: a few plain
`key: value` lines that you read whole. Record what resume needs and Git cannot
show, for example:

```text
profile: medium
phase: implementation
status: paused
task: T2
developer: codex sol low
code reviewers: claude opus medium
reviewed: 537f44de53
project: docs/projects/mvp.md S4
backlog: docs/backlog/2026-10-24-item.md on master
```

Use `status` only for `paused`, `blocked`, `complete`, or `cancelled`. Derive
worktree and branch from Git. The base of the change is the parent of the first
commit that added the plan directory:
`git rev-parse "$(git rev-list --reverse HEAD -- docs/plans/<plan> | head -1)^"`.
Model choices never go into the contract or plan. Older plans have `state.json`
instead; read it the same way and write `state.txt` when updating them.

`findings.md` holds unresolved findings, their evidence, and user-accepted
dispositions only when they must survive a session. Keep one current file and
remove findings once resolved.

## Complete a flow

Before marking a flow complete, add a concise outcome to `plan.md` or
`problem.md`: what was delivered or why no change was warranted, links to
the relevant commits, actual verification, material limits, and any implication
for dependent work. Then write the completion state and commit both.

When cancelling a flow that took a backlog item, move the item back to its
original path on the recorded branch, add what the flow learned, and commit
only that file there.

## Resume

A selected plan's path gives the checkout for every later tool and agent. Check
that the worktree exists, its branch contains the plan's commits, and the plan
files are present. Read state, contract, plan, findings, current diff, and
relevant commits, and determine what actually finished; the state file may be
stale. Rerun any check whose result is not retained. If an agent may still be
running, account for it first. Ask only what cannot be inferred.

When resuming at implementation, use the recorded developer choice, or choose
as described in [coordinator.md](coordinator.md#choosing-a-model) if it is
absent or unavailable on this platform. If code changed after a clean
review, reassess the affected scope before delivery. Do not push, merge, delete
branches or worktrees, or move plan directories as routine cleanup.
