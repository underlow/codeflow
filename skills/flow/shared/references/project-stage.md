# Project stage integration

Read this file only when the user supplies a project document or the selected
flow's `state.json` links it to a project. Otherwise skip it.

## Select the stage

A project document and stage ID select that stage's reported problem or desired
work, goal, and relevant project context as input to an ordinary flow. If the ID
is missing, let the user select a stage. Check matching flows in the checkout
and registered worktrees, including completed and cancelled ones. Compare the
current stage goal with their contracts or recorded results, not just their IDs.
Recognize both active and archived project paths (`docs/projects/<slug>.md`
and `docs/projects/completed/<slug>.md`), including the legacy directory form
ending in `<slug>/project.md`, when matching saved flows. If a saved project
path is missing, check its active or archived counterpart before treating it
as lost. Viewing archived results does not reopen a project; explicit reopening
must first return through project to restore its active location and status.
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
and keep this flow's contract, plan, review, and completion independent. Do not
infer a profile from the roadmap, silently change its other stages, or
automatically start the next stage.

## Register the started work

Once the user chooses to start the stage and its checkout is settled, create its
plan directory and atomically write an initial `state.json` before substantive
investigation. Capture the exact `base_commit` before flow changes and record
`project` (repository-relative path), `stage`, and `phase: analysis`; include
`profile` if already chosen, otherwise omit it until selection. Commit this
registration with explicit paths so a new project session can discover the work
even if analysis is interrupted. This registers started work; it does not mark
analysis complete or require an implementation plan. Carry `project` and `stage`
through later state updates.

## Complete the stage

Completing a linked flow also requires updating that stage in the project
document in the flow's checkout. Record its status, concise outcome, and a link
to this flow plan; preserve prior flow links and unrelated stages. Compare the
stage's current goal with the flow's contract and outcome before marking it
complete. Record an agreed no-change conclusion as such; do not mark unresolved
or changed scope complete. Commit the stage update with the flow's outcome and
completion state before reporting delivery. This update needs no separate
`/project` invocation and does not depend on merge or push. If the project
document or stage cannot be resolved, preserve the flow result and report the
overview update as blocked rather than claiming it was synchronized.

Use the flow's checkout; do not modify another worktree or merge just to publish
the overview. Project reconciles other branches on return and handles project
archival and consequential changes to future stages. Do not start the next stage
automatically.
