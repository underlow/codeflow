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

## Findings

Merge duplicates and check each finding's scope and evidence yourself. Bring to
the user the findings whose correction or acceptance is a real product or risk
decision. When a reviewer rates a problem high but the user accepts its
demonstrated consequence, show the exact scenario and both assessments, and
record the decision. Do not reopen an accepted risk without new evidence. An
unresolved requirement conflict needs correction or explicit acceptance
regardless of its label. Give the fixer only the findings selected for
correction, in the reviewers' original wording.

After a fix, choose fresh review of the corrected behavior and whatever the fix
affected; a targeted reviewer checks the complete current behavior of its scope.
Broaden review when a fix changes shared behavior. When another broad round has
uncertain value or the same findings keep returning, ask the user instead of
looping.

Reuse the reviewers' chosen preset in later rounds unless the user changes it.

## Simplification

After the whole-change reviews and their corrections are resolved, assign a
separate reviewer `review-simplification` for the complete implementation in
every profile. This is a review, not permission to edit code. For a small change,
keep it brief.

Verify its findings and give the justified corrections to a developer using
`fix`. A fresh reviewer using `review-change` with `aspects/behavior` and, when
tests changed, `aspects/test-quality` then checks the corrections and affected
behavior before delivery. No changes are required when there is no justified
simplification.
