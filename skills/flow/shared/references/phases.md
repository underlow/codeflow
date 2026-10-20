# Development phases

These profiles guide depth and handoffs. Move forward when the phase's result is
usable; return to an earlier phase when new evidence invalidates its contract.
Do not invent an outcome merely to satisfy a route. A blocker requires a real
missing decision, evidence, or capability; report what remains possible.
Use [the detailed prompt map](prompt-map.md) for the substantive questions and
checks of each phase.

| Profile | Analysis and planning | Development and review |
| --- | --- | --- |
| `full` | Agree concept, observable requirements and acceptance examples, consequential design, then an ordered plan. Independent challenges are useful at each contract boundary. | Implement bounded tasks; check task results where dependency risk warrants it; review the complete change with reviewers selected for its risks. |
| `medium` | Agree one specification covering behavior and design, independently challenge it, then plan tasks. | Implement tasks and integration; select whole-change reviewers by risk. |
| `small` | Agree concise behavior and acceptance examples, then the technical approach and work in a short plan. | Implement and independently review the change. |
| `bugfix` | Reproduce or otherwise establish the failure, agree expected behavior and correction scope. | Fix, verify the original failure and nearby behavior, then independently review. |

## Analysis

Investigate the existing repository before settling requirements. The user owns
consequential behavior, scope, compatibility, and tradeoffs. Capture the actual
agreement in a durable contract: `concept.md`, `requirements.md`, and `design.md`
when their separation helps for `full`; `specification.md` for `medium`;
`requirements.md` for `small`; `investigation.md` for `bugfix`. Use only the
documents needed to make the next phase independent of conversation history.
State observable behavior, important limits, and concrete acceptance examples.
Independent review may expose missing cases, but put accepted cases in the
contract, not only in a review report. Revise the contract after a consequential
user decision; do not leave contradictory versions as simultaneous authority.

## Planning

Inspect affected code and dependencies. Write `plan.md` with the result to
deliver, approach where needed, ordered work, integration points, and verification
that would catch plausible harmful mistakes. Create `tasks/` only when separately
bounded work really helps a new developer; a small change or bugfix may need only
the plan or investigation. Tasks must make sense without the planning chat.
Prefer observable outcomes over prescribed private helpers or test bodies. Review
plans independently when uncertainty, size, or integration risk warrants it.
Resolve important findings and commit the final plan and contract. Then present
the mandatory coordinator-session choice in [coordinator.md](coordinator.md).

## Development

Start each implementation assignment in a fresh native agent with the committed
contract and plan, the exact task and checkout, and relevant repository rules.
The agent inspects the current code, preserves unrelated changes, implements the
agreed behavior, runs meaningful checks, and commits only its own completed work.
The coordinator checks the returned commit and result before dependent work.
When a plan becomes inaccurate, keep valid implementation, revise the plan and
obtain user agreement for changed consequential decisions. A revised, committed
plan again reaches the coordinator-session choice before more implementation.

## Review and correction

Use [review.md](review.md) for independent code review, finding disputes,
corrections, and selective re-review. A reviewer supplies evidence; the
coordinator checks overlap and scope, the fixer verifies each claimed defect,
and the user decides genuine product tradeoffs. The fixer runs checks appropriate
to its changes. A fresh reviewer assesses the correction and any affected
interactions. A fix is not accepted merely because its author reports success.

## Delivery

Confirm the delivered behavior against the contract and actual validation.
Update maintained documentation only when behavior or usage changed. Explain
unavailable checks and accepted limitations. Record the completion state and
report the result to the user. No separate documentation report, consolidation
report, handoff report, or retrospective is required. Do not claim delivery when
a crucial requirement remains unresolved.
