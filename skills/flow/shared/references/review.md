# Independent review

Inspect the diff before proposing the review plan to the user. For `medium`
and `full`, assign independent reviewers for behavior and integration
(`aspects/behavior`) and for code quality (`aspects/code-quality`). For
`small` and `bugfix`, one reviewer may cover both when the scope is manageable.

Assign `aspects/test-quality` to the behavior reviewer for a few focused checks.
Use a separate test reviewer when assessing coverage is substantial, for example
with complex fixtures, extensive expectation changes, or claims that existing
tests protect several new paths. Judge the verification effort even when the
test diff is small. If code quality review spans more than one reviewer can
inspect in context, divide it by subsystem and give each reviewer the full
code-quality checklist and the relevant callers across its boundaries.

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

Use the same revision for both passes in every profile:

1. Give a separate reviewer `review-simplification`, the original goal, the
   contract and the complete change. Keep the current round's other reports
   and suggested fixes out of this assignment. The reviews may run in parallel.
2. Once all independent reports are in, send the other findings and evidence
   to the same simplification reviewer as a follow-up. Keep their session
   available until they reply. Ask for a brief recommendation: which problems
   warrant local fixes, which call for reconsidering the approach, and which
   proposed fixes depend on unverified assumptions about what users see or
   could lose? Ask what evidence would settle any consequential uncertainty.

Check the recommendation against the evidence and decide which corrections to
assign. Keep the review proportionate to the change.

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
