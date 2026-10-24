# Development phases

These profiles guide depth and handoffs. Move forward when the phase's result is
usable; return to an earlier phase when new evidence invalidates its contract.
Do not invent an outcome merely to satisfy a route. A blocker requires a real
missing decision, evidence, or capability; report what remains possible.
See [detailed prompts](#detailed-prompts) for the substantive questions and
checks of each phase.

Terms used throughout: a *phase* is `analysis`, `planning`, `implementation`,
`review`, or `delivery`; a *stage* is only a project stage. The *contract* is
the agreed behavioral documents (concept, requirements, design, specification,
or investigation); a *shared contract* is information several components or
tasks must agree on. *Acceptance examples* have A IDs. A *task* is one planned
assignment for one fresh developer.

| Profile | Analysis and planning | Implementation and review |
| --- | --- | --- |
| `full` | Agree concept, observable requirements and acceptance examples, consequential design, then an ordered plan. Independent challenges are useful at each contract boundary. | Implement bounded tasks; check task results where dependency risk warrants it; review the complete change with reviewers selected for its risks. |
| `medium` | Agree one specification covering behavior and design, independently challenge it, then plan tasks. | Implement tasks and integration; select whole-change reviewers by risk. |
| `small` | Agree concise behavior and acceptance examples, then the technical approach and work in a short plan. | Implement and independently review the change. |
| `bugfix` | Reproduce or otherwise establish the failure, agree expected behavior and correction scope. | Fix, verify the original failure and nearby behavior, then independently review. |

## Detailed prompts

The [prompt library](../prompts/underlow/) holds the substantive questions,
document structure, and quality criteria for each kind of work. Read the
relevant prompts before doing or assigning that work. Who acts, which files are
written, when to commit, and what happens next are governed by the rest of this
file, [execution.md](execution.md), and [review.md](review.md).

The executor column says who uses each prompt. `coordinator` means you do the
work in this conversation with the user. `developer`, `reviewer`, and `fixer`
are fresh native agents; give them the prompt with their assignment as
described in [coordinator.md](coordinator.md) and [review.md](review.md). A
developer or fixer reports `done`, `needs-decision`, or `blocked` as defined in
[developer.md](developer.md); you decide what happens next.

| Phase and profile | Prompt | Executor |
| --- | --- | --- |
| Full analysis | `01-discover`, `03-requirements`, `05-design-approach` | coordinator |
| | `02-challenge-concept`, `04-review-requirements`, `06-review-design` | reviewer |
| Medium analysis | `22-specify-medium` | coordinator |
| | `23-review-medium-spec` | reviewer |
| Small analysis | `24-specify-small` | coordinator |
| Bug investigation | `32-investigate-bug` | coordinator |
| Full planning | `08-plan-code`; `10-review-plan-with-user` when discussing the plan | coordinator |
| | `11-review-plan` | reviewer |
| Medium planning | `25-plan-medium` | coordinator |
| Small planning | `26-plan-small` | coordinator |
| Medium or small planning | `27-review-compact-plan` | reviewer |
| Full implementation | `12-implement` | developer |
| | `13-review-task` when task dependency risk warrants it, with `15-review/aspects/test-quality.md` when tests changed | reviewer |
| Medium or small implementation | `28-implement-compact` | developer |
| Bug correction | `33-fix-bug` | developer |
| Whole-change review | `15-review` with selected `15-review/aspects/*.md`; `29-review-single` for one combined reviewer | reviewer |
| Correct findings | `17-fix` for full; `30-fix-compact` for medium or small; `33-fix-bug` for bugfix | fixer |

Each numbered directory contains `prompt.md`. Use only the prompts relevant to
the current work. An aspect file supplements `15-review/prompt.md` for a
reviewer with that focus; no aspect requires its own reviewer. The `behavior.md`
aspect covers completeness, correctness, reliability, and connections between
components.

## Analysis

Investigate the existing repository before settling requirements. The user owns
consequential behavior, scope, compatibility, and tradeoffs. Capture the actual
agreement in a durable contract: `concept.md`, `requirements.md`, and `design.md`
when their separation helps for `full`; `specification.md` for `medium`;
`requirements.md` for `small`; `investigation.md` for `bugfix`. Use only the
documents needed to make the next phase independent of conversation history.
State observable behavior, important limits, and concrete acceptance examples.
Independent review may expose missing acceptance examples, but put accepted
examples in the contract, not only in a review response. Revise the contract after a consequential
user decision; do not leave contradictory versions as simultaneous authority.

### Agreeing a document with the user

These rules apply to every document you agree with the user: concept,
requirements, design, specification, investigation, and a plan.

- Inspect the affected repository code, tests, and instructions before proposing
  behavior or technical decisions. Resolve factual and routine engineering
  questions yourself. Ask the user only for missing intent, constraints, or
  consequential choices that evidence cannot answer, and reuse answers already
  given.
- Bring each consequential choice with options, their concrete effects, and a
  recommendation where supported. Ask focused questions, normally one at a time.
- Present the consolidated proposal in the conversation, in manageable pieces
  when it is large, and wait for explicit confirmation of the current version
  before writing the document. Silence or confirmation of an earlier draft is
  not approval.
- When a review, a later phase, or new evidence requires a revision, verify each
  finding's trigger, reachability, and consequence first. A reviewer's priority
  label alone is not a reason to change the document. Correct the general rule,
  not only the reported example: identify every rule, decision, and acceptance
  example the change affects, recheck them against the revised document, and
  resolve contradictions the correction exposes. Preserve unaffected decisions.
  Discuss changed consequential decisions with the user; local repairs within an
  agreed contract need no renewed decision. Tell the user which findings you
  rejected and why.
- Fold accepted corrections into the current text. Do not keep finding history,
  review chronology, obsolete alternatives, or separate decision, evidence, or
  fixes files.
- Record the confirmation and any explicit delegations in the document. Preserve
  the initial request and any supplied source link.
- Commit the agreed document in a focused commit with explicit paths.

When a document turns out to need a change that belongs to an earlier document,
such as a behavioral change discovered during design or planning, explain the
conflict and the decision needed to the user and revise the earlier document
first.

For a project stage, independently check its reported problem and assumptions.
Analysis may show that a bug is not confirmed or a proposed change is unwarranted.
Present the evidence and agree the disposition with the user. If no change is
warranted, record the conclusion and its evidence and limits in the analysis
document and complete the flow without inventing implementation or code review.
Do not call it a fix or treat unavailable reproduction as proof of no defect.
If the result invalidates later stages, explain the implication for the project
plan without silently changing their scope.

## Planning

Inspect affected code and dependencies. Write `plan.md` with the result to
deliver, approach where needed, ordered work, integration points, and verification
that would catch plausible harmful mistakes. Create `tasks/` only when separate
files help a new developer; tasks may instead be numbered sections of `plan.md`.
Choose task boundaries by independently verifiable results and dependencies,
not by the number of files. One plan file does not imply one implementation
assignment. Use a single task only when the change is one bounded result; a small
change or bugfix may need only the plan or investigation. Tasks must make sense
without the planning chat.
Prefer observable outcomes over prescribed private helpers or test bodies. Review
plans independently when uncertainty, size, or integration risk warrants it.
Resolve important findings and commit the final plan and contract. Then present
the mandatory coordinator-session choice in [coordinator.md](coordinator.md).

## Implementation

Assign each planned task to its own fresh developer as described in
[coordinator.md](coordinator.md). Start each assignment with the committed
contract and plan, the exact task and checkout, and relevant repository rules.
Check the returned commit and result before dependent work. When a developer
reports `needs-decision` or the plan otherwise becomes inaccurate, keep valid
implementation, revise the plan, and obtain user agreement for changed
consequential decisions. A revised, committed
plan again reaches the coordinator-session choice before more implementation.

## Review

Use [review.md](review.md) for independent code review, finding disputes,
corrections, and selective re-review. A reviewer supplies evidence; the
coordinator checks overlap and scope, the fixer verifies each claimed defect,
and the user decides genuine product tradeoffs. The fixer runs checks appropriate
to its changes. A fresh reviewer assesses the correction and any affected
interactions. A fix is not accepted merely because its author reports success.

## Delivery

Confirm the delivered behavior against the contract and actual validation.
Check that maintained documentation was updated where behavior or usage changed.
Retain the concise outcome in an
existing flow document and commit it with completion state as described in
[execution.md](execution.md). If this flow is explicitly linked to a project
stage, update that stage's overview in the same checkout and completion commit
as described in [project-stage.md](project-stage.md); standalone flows require
no project. Do not claim delivery when a crucial requirement remains unresolved.

Report the result to the user in plain language:

1. Delivered outcome: what users can now do, against the agreed contract.
2. Verification: what checks and reviews actually established. Base claims on
   evidence that applies to the final implementation; an earlier passing check
   or a developer's completion claim is not proof, and planned checks did not run.
3. Unmet requirements, deviations, accepted limitations, and failed or missing
   checks, when present: their consequence for users and the decision or work
   still needed. Recording an issue does not resolve it or imply approval.
4. Documentation changed, or why none was needed.

Distinguish implemented behavior, verified behavior, and behavior the user
accepted. State readiness only to the extent the evidence supports.
