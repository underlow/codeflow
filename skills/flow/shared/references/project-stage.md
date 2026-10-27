# Project stage integration

## Select the stage

A project document and stage ID supply the stage's problem or desired work, its
goal, and relevant project context as input to an ordinary flow. If the ID is
missing, let the user choose a stage. A description file with `Project:` and
`Stage:` fields also identifies one; check that the selection is still current.

Project documents live at `docs/projects/<slug>.md`, or `<slug>/project.md` in
the older directory form, and move under `docs/projects/completed/` when
archived. If a saved project path is missing, check the other location before
treating it as lost. Viewing archived results does not reopen a project; reopening
goes through the project skill first.

Before starting, look for flows for the same stage in every worktree, including
completed and cancelled ones, and compare their contracts or outcomes with the
current stage goal, not just the IDs. Resume unfinished work instead of
duplicating it. If the stage is already complete, show its outcome and ask
whether the user wants to inspect it or reopen the work. Reopened work is a new
flow that references the earlier result in its analysis document; never rewrite
a finished flow or silently restart a cancelled one. A materially different goal
needs a new stage ID agreed in the project plan first.

## Verify premises

Agreement on a roadmap does not establish that a reported bug exists, a proposed
cause is correct, a change is necessary, or a dependency is required. Verify the
stage's premises during analysis, including whether required earlier results
exist in this checkout. Analysis may show that no change is warranted: present
the evidence, agree the conclusion with the user, record it with its evidence and
limits in the analysis document, and complete the flow without implementation or
review. Unavailable reproduction does not prove there is no defect. If the result
affects later stages, explain the implication without changing them.

Choose the profile with the user; do not infer it from the roadmap.

## Register the started work

When the flow starts its work, the initial `state.json` also holds `project`
(repository-relative path) and `stage`, so a later project session can find the
work. Keep them in every later state update.

## Complete the stage

Completing the flow also updates that stage in the project document in the
flow's checkout: its status, a concise outcome, and a link to this plan, keeping
earlier flow links and other stages intact. Compare the stage's current goal
with the flow's contract and outcome first; record an agreed no-change
conclusion as such, and do not mark unresolved or changed scope complete. Commit
the stage update together with the flow's outcome and completion state. If the
project document or stage cannot be resolved, keep the flow result and report the
project update as blocked.

Do not modify another worktree or merge to publish the update, change other
stages, or start the next stage. The project skill reconciles branches and
handles archival.
