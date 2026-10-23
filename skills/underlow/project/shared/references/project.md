# Project goal and stage plan

`project` helps the user organize intended work into a high-level project goal
and stages, maintain that plan, and choose the next stage. Clarify the request
only enough to describe the goal, stage boundaries, and logical order. All
investigation belongs inside the selected stage's ordinary `flow`.

Do not reproduce bugs, inspect application code, research feasibility or causes,
choose technical solutions, define API details, or delegate such work while
forming the project plan. Existing conversation may supply context; preserve
its provenance and distinguish reported facts, hypotheses, and user decisions.
The user's desired behavior can be specific without prescribing implementation.
Do not choose flow profiles or write implementation plans here.

## Find or establish the project

Find the current Git repository and registered worktrees with
`git worktree list --porcelain`. A path argument selects an existing
`docs/projects/<slug>.md` or an archived project under `docs/projects/completed/`;
an optional stage ID selects a stage. Also accept existing projects at
`docs/projects/<slug>/project.md`. Without an argument, find active project
documents in the current checkout and registered worktrees; let the user choose
if several could match. Exclude `completed/` from the active list, but inspect
it when the user asks for a finished project or no active project matches.
Record the selected
checkout and use it for subsequent work; a worktree does not change the session's
cwd. Do not silently adopt unrelated plans or missing worktrees.

For a new project, help express its goal and split the intended work into
separately selectable stages. A stage is a meaningful piece of work, not a
minimum size or a technical task. Do not invent stages to reach a count or make
independent requests artificially dependent. Suggest logical ordering from the
stated scope; leave uncertain dependencies tentative rather than investigating
them. The user owns the goal, boundaries, and consequential ordering decisions.

For five reported bugs, make five stages without checking that they are bugs.
Each flow may confirm and fix its report, or conclude that no change is warranted.
For a large application, include a stage to agree the API before stages that
implement or consume it, without deciding the API here. Frontend work that does
not require that API may come earlier. Clarify an ambiguous stage only enough to
understand its dependency.

Keep one `docs/projects/<slug>.md` directly in `docs/projects/`, without a
per-project directory, containing:

- the project goal;
- shared context and constraints needed to understand the plan;
- stages with stable IDs, each describing the reported problem or requested
  work and its goal, plus material boundaries and dependencies when relevant;
- stage status, a concise outcome when known, and links to associated flow plans.

Detailed acceptance criteria, reproduction, requirements, design, implementation
plans, and task breakdowns belong to flow. Do not duplicate those documents in
the project or create stage handoff files or a separate decision log.

Near the top of every project document, explicitly warn its future flow reader:

> This is a high-level plan based on the user's request. Reported bugs,
> assumptions about causes, technical necessity, and dependencies have not been
> verified; stage order is provisional. Agreement on this document approves the
> intended direction, not its technical claims. Each stage's flow independently
> checks its premises, refines its scope, and determines whether to implement,
> fix, propose no change, or recommend revising the project plan.

Retain this distinction even when some context has evidence: identify the source
and limits of that evidence. The user's agreed goals remain goals, not claims
that require technical proof.

Once the user agrees on the plan, commit the project document in a focused
commit and offer to start a selected stage now or provide the command for a new
session. Preserve unrelated changes. Do not push, merge, or remove worktrees as
routine project work.

## Return to a project

Flow's coordinator records execution state and a durable outcome in its own
plan. When the flow is explicitly linked to a project stage, it also updates
that stage's status, concise outcome, and flow link in the project document in
its checkout as part of completion, without waiting for a separate project
invocation. Project reconciles the overview on return, including flows from
other branches and older flows that did not update it. Read the project document
and inspect linked flow plans. Also look
in `docs/plans/` in the selected checkout and registered worktrees for native plans
whose `state.json` has the matching `project` path and `stage` ID, including initial
registrations without a selected profile. Match both the active and archived
paths of the same project so moving it does not hide earlier flows, including
those in other worktrees. Existing links may omit a just-started
or reopened flow, so do not search only when links are missing.
Use plan state, recorded conclusions, and relevant Git history to establish what
finished; do not audit application code or rerun checks just to open the project.
A stale pointer alone is not a reason to repeat valid work. If a plan or worktree
is missing, report the uncertainty. Resolve competing plans for one stage rather
than choosing one by date.

Update the stage overview from these results. A stage can be complete because a
reported defect was not confirmed or an agreed investigation concluded no change
was warranted; record that disposition rather than calling it fixed. Do not mark
unresolved or merely abandoned work complete. A completed flow on another branch
is not automatically an available dependency in the checkout for the next stage.
Completion also does not imply that a dependent stage's premise remains valid:
for example, concluding that an API is unnecessary does not make its planned
implementation ready to start. Flag affected stages for reconsideration. If a
required outcome is unavailable or unclear, explain this before proposing the
dependent work; its flow verifies technical availability before relying on it.

Compare the current stage goal with the linked flow's contract and outcome.
An old completion applies only to the work it actually covered. If a goal has
changed, do not copy the old completion onto the new scope. Commit actual
overview updates, including statuses, concise outcomes, and flow links, in a
focused commit before offering the next work. Do not create an empty commit
when nothing changed or commit unrelated user edits in the project document.

Offer to continue an unfinished stage's existing flow in this session. If there
is one next eligible stage, propose starting it here; if several independent
stages are available, offer the user a choice. Explain missing dependencies and
what remains possible. Do not automatically start work on opening the project or
automatically chain stages after one finishes. A new session is optional.

## Complete or reopen a project

When refreshing the overview establishes that every stage is complete or has
been explicitly superseded, mark the project complete and move
`docs/projects/<slug>.md` to `docs/projects/completed/<slug>.md`. For an existing
project at `docs/projects/<slug>/project.md`, move the whole project directory
to `docs/projects/completed/<slug>/`, preserving any contents. Do not archive
a project with unresolved, paused, blocked, cancelled, or reopened work merely
because no flow is running. Archive as part of the completion update without an
additional permission step. Flow updates its own stage at completion; project
performs the project-wide reconciliation and move on return, including after
the final stage.

Preserve the document, stage IDs, outcomes, and flow history. Repair relative
links in the moved document and references to it in the selected checkout,
including matching flow state `project` paths. Do not change execution statuses
or rewrite other worktrees; recognize their old project paths during discovery.
Never overwrite an existing archive destination. Commit the move, overview,
and reference updates together, preserving unrelated changes, and report the
new path. Viewing an archived project leaves it archived.

If the user explicitly reopens a stage or adds new work to an archived project,
move it back to its original active location, update its status and references
by the same rules, and commit these changes before starting or resuming flow.
Do not overwrite another active project or silently reopen completed work.

## Start or resume a stage

Use the project document and selected stage ID directly as flow's input. For a
new stage, offer `$flow docs/projects/<slug>.md S1` in Codex or
`/flow docs/projects/<slug>.md S1` in Claude Code, using the actual document
path for an existing project. For an existing flow,
resume its plan instead of starting a duplicate. Check terminal flows too: when
the selected stage is already complete, show the result and distinguish viewing
it from explicitly reopening work. Do not silently restart completed or cancelled
work. Give the exact checkout and command when the user chooses a new session.

When the user chooses to continue here, load and follow the installed `flow`
skill's instructions in this conversation with that input. This is an ordinary
flow with its own profile selection, investigation, contract, plan, execution,
and review. Do not launch it as a project subagent, require a separate session,
or perform its investigation under project rules first. Pass through the
project's warning about unverified premises. Before dependent work starts,
flow checks that required prior results are actually available in its checkout.

## Reconsider the plan

When a flow result invalidates a premise or the user changes direction, explain
which future stages or dependencies are affected and propose the necessary plan
changes without doing their investigation. Obtain the user's decision on
consequential changes, then edit and commit the project document. Preserve stable
IDs for unchanged stages and mark superseded stages so their existing flows
remain understandable. Use Git for earlier plan versions.

For a materially different goal, create a new stage ID and preserve the old
stage's outcome and flow link. If the user explicitly reopens the same goal,
mark it reopened, retain its prior result, and link the new flow separately;
the prior completion must not make the reopened work appear finished. The same
rule applies when an active stage's goal changes: do not silently reuse its old
contract for the new scope.

Changing the project plan never silently changes an active flow's agreed
contract. Bring a changed goal to that flow explicitly for replanning. Project
status summarizes the work; the flow's contract, recorded conclusion, and Git
remain the source for its execution and results.
