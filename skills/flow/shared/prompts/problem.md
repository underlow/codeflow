Understand the problem with the user before any profile is chosen: what is
asked, how the system behaves now, what is wrong or missing, and the rough size
of the work. Every flow starts here; the profile is chosen from the agreed
result.

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
4. Desired result: the problem, who is affected, and the intended outcome.
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
