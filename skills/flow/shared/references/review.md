# Independent review

Before the first code review, the coordinator proposes a concrete review plan to
the user: what changed, which risks deserve a separate reviewer, and which can
be covered together. Include a concrete available model and reasoning effort
for each proposed reviewer, with a short reason where the choice matters. Wait
for the user's selection or agreement on both the reviewers and their model
settings before launching them. The development choice is not automatically
the review choice. Consider behavior across supported entry paths, test quality,
security, performance, and
code quality. Behavior includes completeness, logic, reliability, and component
connections. These are review questions, not five mandatory agents or reports.
Use specialists when the change gives them a real question to answer.

## Give each reviewer a bounded assignment

Include the exact checkout, base and current commits, run-owned changes, agreed
contract and acceptance examples, selected focus, relevant previous findings and
corrections, user-accepted risks, and validation evidence. Say whether focused
checks are safe in this checkout. Do not send the entire planning conversation.
The reviewer must separate unrelated user changes and state any missing evidence.
For a new session, do not claim a prior check passed without retained evidence.

The reviewer inspects the whole assigned scope, not just the last commit or the
file that first drew attention. Trace relevant entry paths, inputs, state,
failures, retries, downstream uses, and observable results. If a defect uses
shared logic, check other reachable uses. Finding one issue is not a reason to
stop. A reviewer may report a credible issue outside the assigned focus rather
than hide it because another aspect might own it. The coordinator decides whether
it needs another specialist.

A reviewer may run a focused test or reproduction when it would settle a material
doubt and can be done safely in an isolated or disposable environment. Do not
change product code, commit, use production data, or run destructive checks.
Name the command or action, its observed result, and its limit. Inspect existing
validation evidence, but do not repeat a broad suite merely to claim coverage.
Missing evidence is not a passing check.

## Report facts before priority

Return findings in the final response, not a report file. For each finding give:
location or missing behavior; reachable trigger; evidence or a check that would
distinguish it; likely consequence; uncertainty; and the required behavior or
question for the user. Recommend urgency only after explaining those facts.
A high label is not a decision to fix. Do not inflate a finding from a theoretical
worst case, a hypothetical workload, or a preferred design. A credible risk of
data loss, security breach, or another irreversible consequence must be stated
plainly even if the user may choose to accept it.

If there are no findings, say so. Add only a brief account of what behavior or
risk was checked and what could not be checked. Do not produce a per-operation
coverage table, file inventory, reading log, design for the fixer, or history of
resolved findings. Reuse a finding ID only when it helps compare a persistent
problem with prior review. Reviewers do not edit project files or commit.

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
