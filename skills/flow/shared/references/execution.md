# Workspace, state, and resume

## Resolve a request

List the repository's worktrees with `git worktree list --porcelain`. An
argument may name a plan directory in any worktree, a description file, or a
project document with a stage ID, such as `docs/projects/app.md S12`; ask about
an argument that matches none. Without an argument, look for unfinished plans in
`docs/plans/` of every worktree and show each one's feature, profile, phase,
branch, and absolute path. A plan is recognized by its `state.json`. Completed
and cancelled plans are terminal. A backlog item file as the request is the
flow's source document.

For a new request, first discuss the task with the user and inspect the
repository until the problem, the desired result, and the rough size are clear.
Only then propose a profile with a short reason and let the user choose; do not
ask for it earlier. Until the user confirms the first contract document, create
no branch, plan directory, state, or commit; keep experiments outside the
repository or remove them. On that confirmation, start the work:

1. Choose a `flow/<slug>` branch in the current checkout by default, adding a
   suffix if the name is taken. If the user's uncommitted changes would overlap,
   offer a separate worktree or let them resolve it; never stash, discard, or
   commit their work. Before creating a worktree, tell the user if the analysis
   relied on uncommitted changes it will not contain.
2. For a backlog item, move it into the plan directory as `backlog-item.md` and
   commit only that move on the current branch, so other checkouts stop
   offering it.
3. Create the branch or worktree, write the document and `state.json`, and
   commit them. Record the item's original path and the branch from step 2 as
   `backlog` in `state.json`.

In a worktree, pass its absolute path to every tool and agent.

When the user supplies a project document or the plan's state names a project,
also follow [project-stage.md](project-stage.md). Otherwise ignore project
documents.

## Plan directory

Each plan lives in `docs/plans/<date>-<slug>/` and holds only the contract
documents, `plan.md` with optional `tasks/`, `state.json`, `backlog-item.md`
when taken from the backlog, and `findings.md` when needed. Routine progress
lives in the conversation and Git history.

Besides the backlog item move, commit only at these points, always with explicit
paths: the first contract document with the initial state; the remaining
contract documents and the plan together once planning is finished; each
developer's completed task; and the outcome with the completion state.

## State

You alone write `state.json`, atomically, after the work it records exists. It
holds `profile` and `phase`; `task` only while a task is active; `status` only
for `paused`, `blocked`, `complete`, or `cancelled`; `codex` with the roles
assigned to Codex, if any; `backlog` for a taken backlog item; and a reviewed
commit when you need to know whether later code invalidated a clean review.
Derive worktree and branch from Git. The base of the change is the parent of the
first commit that added the plan directory:
`git rev-parse "$(git rev-list --reverse HEAD -- docs/plans/<plan> | head -1)^"`.

After the user confirms development agent settings, store them as
`development_agent` with `platform`, `model`, and `effort`, plus an optional
`tasks` object for per-task exceptions the user chose. If the user stops after
confirming a review plan but before reviewers start, keep the pending reviewer
choices with their scope and commit; discard them when the scope changes or the
review starts. Model choices never go into the contract or plan.

Example after stopping at the committed plan:

```json
{
  "profile": "medium",
  "phase": "implementation",
  "status": "paused"
}
```

`findings.md` holds unresolved findings, their evidence, and user-accepted
dispositions only when they must survive a session. Keep one current file and
remove findings once resolved.

## Complete a flow

Before marking a flow complete, add a concise outcome to `plan.md` or the
analysis document: what was delivered or why no change was warranted, links to
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

When resuming at implementation, use the stored development settings, or ask for
them if absent or unavailable on this platform. If code changed after a clean
review, reassess the affected scope before delivery. Do not push, merge, delete
branches or worktrees, or move plan directories as routine cleanup.
