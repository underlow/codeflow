# Independent review

Before the first code review, the coordinator proposes a concrete review plan to
the user: what changed, which risks deserve a separate reviewer, and which can
be covered together. With it, ask for the reviewers' model as in
[coordinator.md](coordinator.md#choosing-a-model); one choice covers all
reviewers of the round unless the user wants otherwise. Wait for agreement on
both before launching them. Risks to consider: behavior across supported entry paths
(completeness, logic, reliability, component connections), test quality,
security, performance, and code quality. Add a specialist only when the change
gives it a real question.

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
