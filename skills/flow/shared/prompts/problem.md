Understand the problem with the user before any profile is chosen: what is
asked, how the system behaves now, what is wrong or missing, and the rough size
of the work. Every flow starts here; the profile is chosen from the agreed
result.

Act as a product manager from the start of this investigation. Treat the request
as input to evaluate: distinguish the user's need and desired outcome from
assumptions, proposed solutions, constraints, and explicit user decisions.
Starting a flow or selecting a project stage does not establish that every
listed change is necessary or that its proposed solution is suitable.

Before asking about details of a proposed solution, form and explain your own
assessment: who benefits in which real scenario, what existing behavior fails
to provide, why the proposed change would help, and whether its benefit warrants
the complexity and ongoing cost. Consider existing capabilities and simpler
ways to reach the outcome. Absence of a feature or inconsistency in internal
wiring alone does not establish a need to change it. Inspect code and other
evidence as needed to make this assessment; do not replace it with an inventory
of missing features or a questionnaire for the user.

Recommend proceeding, changing or simplifying the approach, checking an important
unknown, or making no change, with reasons and evidence limits. If an unknown
could change that recommendation, identify the question, how its answer would
affect the decision, and a proportionate way to check it. Research and prototypes
are useful when they answer such a question, not mandatory steps. Keep this
assessment brief for clear, low-risk work; a user's own need is a valid basis
without market validation. Respect explicit user decisions, raising concrete
new evidence if it challenges them. Discuss consequential conclusions before
planning; `problem.md` records the result of this thinking.

Inspect code, tests, logs, configuration, and Git history. Do not change
application code or production data; use disposable probes. Separate observation
from hypothesis, and never claim a reproduction or probe that did not run.

The affected code was written for a reason. Find out why it behaves this way
from its history, tests, comments, and callers. If the current behavior serves
another case, that case is behavior to preserve. If the reason cannot be found,
say so.

For a reported defect, reproduce it and trace the trigger to its cause. If the
original environment is unavailable, say what was tested instead. Then agree the
smallest coherent correction and think through what it could break before
agreeing it with the user.

For new work, check the premises: what already exists, what is actually
missing, and whether required earlier results are present. Walk through a few
representative user journeys, including failures and interaction with existing
behavior, to find product choices nobody has made yet. Explain findings by their
effect on the user.

Write `problem.md`, each section proportional to the problem:

1. Original request and source.
2. Current behavior: how the affected part works now, why, and behavior to
   preserve with the cases that rely on it.
3. For a defect: expected versus actual behavior, reproduction (prerequisites,
   exact commands or probe code, observed results, limits), and the cause with
   its evidence and remaining hypotheses.
4. Desired result: the problem, who is affected, the intended outcome, and why
   the recommended direction addresses the need, with evidence limits.
5. Scope: included and excluded work, major decisions, supplied constraints, and
   the rough size.
6. For a defect: correction scope and its risks: what changes, other callers,
   cases relying on current behavior, stored data, compatibility, and how the
   correction avoids each. Add changes needing approval, as described in
   [approval.md](../references/approval.md).
7. Open questions, assumptions, and accepted risks, with their consequences.
8. Agreement: current confirmation and explicit delegations.

Keep it short and understandable without code knowledge; code links are fine,
but understanding must not depend on them. Leave exact rules, counts, and
mechanisms to later documents unless they decide scope.

The problem is ready when the user confirms it and no open issue could change
its purpose, scope, or the diagnosis. Then propose a profile with a short reason,
or a split into `project` stages for work over two weeks. If the evidence shows
no change is warranted, agree that with the user and record the conclusion with
its evidence and limits; an unavailable reproduction does not prove there is no
defect. For a defect, this document is the developer's whole contract. When the
fix disproves the cause or changes the scope, update it and reconfirm the
changed decisions.
