# Independent review

Before the first code review, the coordinator proposes a concrete review plan to
the user: what changed, which risks deserve a separate reviewer, and which can
be covered together. Include a concrete available model and reasoning effort
for each proposed reviewer, with a short reason where the choice matters. Wait
for the user's selection or agreement on both the reviewers and their model
settings before launching them. The development choice is not automatically
the review choice. Consider behavior across supported entry paths, test quality,
security, performance, and code quality. Behavior includes completeness, logic,
reliability, and component connections. These are questions to cover, not a
required set of reviewers. Use specialists when the change gives them a real
question to answer.

## Give each reviewer a bounded assignment

Give each reviewer [reviewer.md](reviewer.md), the relevant detailed prompt
from [phases.md](phases.md#detailed-prompts), any selected aspect file, and its
assignment. For code, the assignment names the exact checkout, base and current
commits, unrelated user changes to exclude, agreed contract and acceptance
examples, selected focus, relevant previous findings and corrections,
user-accepted risks, and validation evidence; say whether focused checks are
safe in this checkout. For a document, it names the document, the upstream
contract, and relevant previous findings. Do not send the planning
conversation. In a new session, do not claim a prior check passed without
retained evidence.

## Handle findings

The coordinator groups duplicates, checks scope and evidence, and passes the
original findings to the fixer. The fixer verifies reachability, impact, and
existing protections; it may reject a finding with evidence. The coordinator
and user decide which verified findings require correction. If a reviewer calls
a problem high but the user considers even its demonstrated consequence
acceptable, present the exact scenario and both assessments. Record the user's
disposition and its consequence. Do not reopen the same accepted risk without
new evidence. An unresolved requirement conflict needs correction or explicit
user acceptance regardless of the reviewer's priority label.

After a fix, choose fresh independent review from corrected behavior, prior
findings, and newly affected interfaces. A targeted reviewer checks the complete
current behavior of its scope, not only the last diff. Broaden review when a
correction changes shared behavior or invalidates earlier coverage. File type
alone does not prove an aspect is unaffected. Discuss another broad round with
the user when its value is uncertain; repeated findings or substantive
disagreement need a decision, not an automatic loop.

Reuse a confirmed reviewer's model and effort for the same focus when they still
fit; include any new reviewer or changed setting in the next proposal to the
user. Apply selections through native agent settings. If a selected combination
is unavailable, return to the user with an alternative instead of silently
falling back.
