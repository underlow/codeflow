# Development phases

Phases are `analysis`, `planning`, `implementation`, `review`, and `delivery`.
Move forward when a phase's result is usable; go back when new evidence
invalidates an earlier document. A blocker needs a real missing decision,
evidence, or capability; say what remains possible.

Terms: the *contract* is the agreed behavioral documents (concept, requirements,
design, specification, or investigation); a *shared contract* is what several
components or tasks must agree on. *Acceptance examples* have A IDs. A *task* is
one planned assignment for one developer. A *stage* is only a project stage.

| Profile | Analysis and planning | Implementation and review |
| --- | --- | --- |
| `full` | Agree concept, requirements with acceptance examples, and design, then an ordered plan. Independent challenge is useful after each document. | Implement tasks; review a task result when later tasks depend on it; review the complete change with reviewers chosen by risk. |
| `medium` | Agree one specification covering behavior and design, challenge it independently, then plan tasks. | Implement tasks; choose whole-change reviewers by risk. |
| `small` | Agree concise requirements with acceptance examples, then a short plan with the technical approach. | Implement and review the change independently. |
| `bugfix` | Establish the failure, agree expected behavior and correction scope. | Fix, verify the original failure and nearby behavior, then review independently. |

## Detailed prompts

The [prompts](../prompts/) hold the questions, document structure, and quality
criteria for each kind of work; read the relevant prompt before doing or
assigning that work. `coordinator` means you do it in this conversation. Other
executors are new agents, native or Codex as described in
[coordinator.md](coordinator.md#codex-agents). A developer or fixer reports `done`,
`needs-decision`, or `blocked`; you decide what happens next.

| Phase and profile | Prompt | Executor |
| --- | --- | --- |
| Full analysis | `concept`, `requirements`, `design` | coordinator |
| | `review-concept`, `review-requirements`, `review-design` | reviewer |
| Medium analysis | `specification` | coordinator |
| | `review-specification` | reviewer |
| Small analysis | `requirements-small` | coordinator |
| Bug investigation | `investigation` | coordinator |
| Full planning | `plan-full`; `discuss-plan` when walking the user through it | coordinator |
| | `review-plan-full` | reviewer |
| Medium planning | `plan-medium` | coordinator |
| Small planning | `plan-small` | coordinator |
| Medium or small planning | `review-plan-compact` | reviewer |
| Implementation | `implement` | developer |
| | `review-task` for a full-profile task later tasks depend on, with `aspects/test-quality` when tests changed | reviewer |
| Bug correction | `fix-bug` | developer |
| Whole-change review | `review-change` with selected `aspects/*`, always including `aspects/test-quality` when tests changed, or `review-change-single` for one combined reviewer | reviewer |
| Correct findings | `fix` | fixer |

Each prompt is `prompts/<name>.md`. An aspect adds a focus to `review-change` or
`review-change-single`; no aspect requires its own reviewer.

## Analysis

The user owns consequential behavior, scope, compatibility, and tradeoffs.
Record the agreement in `concept.md`, `requirements.md`, and `design.md` for
`full`; `specification.md` for `medium`; `requirements.md` for `small`;
`investigation.md` for `bugfix`. The next phase must work from these documents
without the conversation. Put accepted acceptance examples from reviews into the
contract itself.

### Agreeing a document with the user

These rules apply to every document you agree with the user, including a plan.

- Inspect the repository before proposing behavior or technical decisions. Ask
  the user only what evidence cannot answer, and do not ask again what they
  already answered.
- Bring each consequential choice with options, their effects, and a
  recommendation. Ask focused questions, normally one at a time.
- Bring each change listed in [approval.md](approval.md) as its own question,
  even when the user already agreed the surrounding text.
- Show the proposal in the conversation and wait for explicit confirmation of the
  current version before writing the file. Silence or approval of an earlier
  draft is not confirmation.
- On revision, verify each finding first; a reviewer's priority label is not a
  reason to change anything. Fix the general rule, not just the reported example,
  and recheck what the change affects. Discuss changed consequential decisions
  with the user; local repairs need no new approval. Tell the user which findings
  you rejected and why.
- Keep only the current agreed text: no finding history, review chronology,
  obsolete alternatives, or separate decision or evidence files.
- Record the confirmation and explicit delegations in the document, and keep the
  initial request and any source link.

When a later document needs a change that belongs to an earlier one, explain the
conflict to the user and revise the earlier document first.

## Planning

Tasks may be numbered sections of `plan.md` or files under `tasks/`. Draw task
boundaries by independently verifiable results and dependencies, not by files;
one plan file does not make one task. Each task must be understandable without
the planning conversation. Get an independent plan review when uncertainty,
size, or integration risk warrants it. When the plan is final, commit the
remaining contract documents and the plan together, then follow the start of
implementation in [coordinator.md](coordinator.md).

## Implementation

Give each task to its own developer with the committed contract and plan, the
exact task, and the checkout. Check the returned commit and result before
dependent work. When a developer reports `needs-decision` or the plan proves
wrong, keep valid work, revise the plan with the user, commit the revision, and
recheck the development model before more implementation.

## Review

Follow [review.md](review.md). A fix is not accepted because its author reports
success; a new reviewer checks it.

## Delivery

Confirm delivered behavior against the contract and actual validation, and check
that documentation was updated where behavior or usage changed. Do not claim
delivery while a crucial requirement is unresolved. Record the outcome and
complete the flow as described in [execution.md](execution.md).

Report to the user in plain language:

1. What users can now do.
2. What checks and reviews actually established for the final code; an earlier
   passing check or a completion claim is not proof.
3. Unmet requirements, deviations, accepted limitations, and missing checks, with
   their consequence and what is still needed.
4. Documentation changed, or why none was needed.

Distinguish implemented, verified, and user-accepted behavior.
