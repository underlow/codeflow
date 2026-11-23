# Independent review

Before the first code review, the coordinator proposes a concrete review plan to
the user. For `medium` and `full`, assign at least two independent reviewers:

- Behavior and integration, using `aspects/behavior`.
- Design, code quality, and test quality, using `aspects/code-quality` and
  `aspects/test-quality`.

For `small` and `bugfix`, one combined reviewer may cover these concerns.
Add specialists for concrete risks such as security and permissions, irreversible
data changes, concurrency, or performance at the expected scale. Explain which
risks need separate review and which the main reviewers can cover.

With the plan, ask for the reviewers' model as in
[coordinator.md](coordinator.md#choosing-a-model); one choice covers all
reviewers of the round unless the user wants otherwise. Wait for agreement on
both before launching them.

## Assignment

Give each reviewer [reviewer.md](reviewer.md), its detailed prompt from
[phases.md](phases.md#detailed-prompts), any selected aspect file, and:

- for code: the checkout, base and current commits, unrelated user changes to
  exclude, the contract, the focus, earlier findings with their corrections,
  accepted risks, existing validation evidence, and whether running checks in
  this checkout is safe;
- for a document: the document, its upstream contract, and earlier findings.

Do not send the planning conversation.

## Whole-change review order

In every profile, verify the whole-change reviewers' findings, then assign
`review-simplification` to a separate reviewer before issuing fixes. Give them
the same complete implementation and the confirmed findings with their evidence.
Leave the choice of remedies open. Keep this review brief for a small change.

Verify the simplification findings and consider both sets together when choosing
corrections for `fix`.

## Findings

Merge duplicates and check each finding's scope and evidence yourself. When a
review finds several problems, pause before revising the document or assigning
fixes. Consider whether one mistake in the requirements,
plan, or implementation could explain them. For a plan, ask whether you would still
propose the revised plan for the original goal. For code, ask whether local
fixes would leave the cause in place. If the findings share a cause, compare
fixing them individually with revising the underlying decision. Handle
independent findings individually.

Bring findings to the user when their correction or acceptance requires a
product or risk decision. When a reviewer rates a problem high but the user accepts its
demonstrated consequence, show the exact scenario and both assessments, and
record the decision. Do not reopen an accepted risk without new evidence. An
unresolved requirement conflict needs correction or explicit acceptance
regardless of its label. Resolve proposed requirement changes before assigning the affected fix.
Give the fixer only the findings selected for
correction, in the reviewers' original wording.

After a fix, a fresh reviewer checks the corrections and affected behavior
using `review-change` with `aspects/behavior` and, when tests changed,
`aspects/test-quality`. Consider another simplification review only if the
corrections materially changed the design.
Broaden review when a fix changes shared behavior. When another broad round has
uncertain value or the same findings keep returning, ask the user instead of
looping.

Reuse the reviewers' chosen preset in later rounds unless the user changes it.
