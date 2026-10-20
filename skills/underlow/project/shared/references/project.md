# Project research and roadmap

`underlow/project` helps the user investigate an idea, keep an evolving map of
stages, choose work, and reconsider the map. A stage is a desired result, not a
`flow` profile or an implementation plan. The user starts a separate ordinary
`flow` session for a selected stage and chooses its profile there. Do not start
that session as a project subagent, schedule later stages, or intervene in a
running flow's implementation and review.

## Find or establish the project

Find the current Git repository and registered worktrees with
`git worktree list --porcelain`. A path argument may select an existing
`docs/projects/<slug>/project.md` or one of its stage handoffs. Without an
argument, find project documents in the current checkout and registered
worktrees; let the user choose if several could match. Do not silently adopt an
unrelated plan or a removed worktree. Record the selected checkout and use it
for subsequent project writes; a worktree does not change the session's cwd.

For a new project, discuss the idea and investigate consequential uncertainties
with the user. Use bounded research agents when they can answer distinct
questions; check their evidence and report uncertainty. The user owns purpose,
scope, consequential tradeoffs, and whether to proceed. The research may show
that development should change direction or stop. Do not manufacture a stage
list merely to make progress.

Keep durable research in one `docs/projects/<slug>/project.md` in the chosen
checkout, including when research spans sessions. Clearly mark tentative
conclusions and proposed stages until the user agrees. The document should
contain:

- the intended outcome and boundaries;
- research conclusions and evidence needed to understand later choices;
- confirmed decisions, material assumptions, and open questions;
- an ordered map of stages with stable IDs, each stage's desired result,
  completion condition, and dependencies.

Only the near-term work needs much detail. A distant stage may remain a named
hypothesis. Do not assign `small`, `medium`, `full`, or `bugfix` profiles, write
future implementation plans, copy research transcripts, or maintain a second
decision log. Commit durable research and agreed changes in focused commits;
do not present tentative work as confirmed. Preserve unrelated changes; do not
push, merge, or remove worktrees as routine work.

## Reconcile before suggesting work

On each return to the project, read its document and inspect registered
worktrees for native flow plans in `docs/plans/` whose `state.json` contains
both this project's repository-relative path and a matching stage ID. Read the
linked plan state and relevant Git evidence; the state may lag actual work.
Distinguish a flow that is active, paused, blocked, or complete from a result
that is present in the checkout where the next stage would run. A completed
flow on another branch is not automatically an available dependency. If a
worktree or plan is missing, report what can and cannot be established rather
than guessing that the stage is done. Do not repeat already valid work because
a pointer is stale.
If a stage has a handoff but no linked plan yet, report only that the handoff
was prepared. If several plans claim the same stage, inspect their branches and
histories rather than choosing one by date; bring an unresolved identity or
result conflict to the user.

Give the user a concise view of current stage results, unavailable dependencies,
and open decisions. Update the project document with durable conclusions and
links to completed flow plans or commits only when the evidence supports them.
Do not duplicate a flow's contract, tests, findings, or review report in the
project. The current flow plan and Git are the source for its execution status;
the project document is the source for the project's purpose and stage map.

## Hand a chosen stage to flow

The user chooses what to work on, including a later stage or a return to
research. Check the chosen stage's current meaning and dependencies. Explain
the consequence of any missing dependency; do not silently reorder the map or
claim unavailable code is present. A stage can be selected despite an unmet
dependency only after the user understands what work is possible now.

For a stage that needs a new flow, write a short handoff at
`docs/projects/<slug>/stages/<stage-id>.md` in the project's checkout. Include
these two unambiguous fields near the top:

```text
Project: docs/projects/<slug>/project.md
Stage: <stage-id>
```

Then state the selected result and completion condition, relevant confirmed
decisions and constraints, dependencies and their actual status, and links to
needed prior results. This is an input description, not requirements, design,
task breakdown, or a preselected flow profile. Commit the handoff. If one
already exists, inspect its linked flow and do not overwrite an active flow's
agreed input; discuss changed scope and return to that flow's planning when
needed.

Give the user the exact handoff path and the selected checkout. Ask them to
start a separate normal session there with `$flow <handoff-path>` in Codex or
`/flow <handoff-path>` in Claude Code. Flow selects its profile with the user,
owns its plan and review, and records the project and stage in its own state.
The project skill stops at this handoff. It does not wait for or automatically
launch the next stage.

## Reconsider the map at any time

On request, compare new evidence, completed results, and the active stage's
contract with the project's goal and assumptions. Propose concrete changes to
future stage results, order, splits, dependencies, or even the goal. Explain
what earlier work remains valid. Obtain the user's decision on consequential
changes, then edit and commit the current project document. Keep stable IDs for
unchanged stages; mark an abandoned stage as superseded when a previous handoff
or flow needs to remain understandable. Git retains earlier maps; do not keep
round-numbered roadmap copies.

Changing the project map never silently changes an active flow's agreed
contract. Identify the conflict and direct the user to that flow to revise or
finish it deliberately. On the next project invocation, reconcile the outcome
again from its plan and Git. Do not treat a project-level replan as evidence
that the code or integration already changed.
