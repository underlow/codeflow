Investigate the reported bug and agree the intended behavior with the user.
Inspect code, tests, logs, and configuration, and try a focused reproduction or
a disposable probe without changing application code or production data. Trace
the trigger to its cause and separate observation from hypothesis. Never claim a
reproduction that did not run; if the original environment is unavailable, say
what was tested instead.

The code being fixed was written for a reason. Before proposing a change, find
out why it behaves this way from its Git history, tests, comments, and callers.
If the current behavior serves another case, that case is behavior to preserve.
If the reason cannot be found, say so. Then think through what the proposed
correction could break before agreeing it with the user.

Write `investigation.md`:

1. Original report and source, expected versus actual behavior, and affected scope.
2. Reproduction: prerequisites, exact commands or probe code, observed results,
   and limits.
3. Cause: evidence, why the code was written this way, affected nearby paths,
   remaining hypotheses, and why the proposed correction addresses the cause.
4. Fix scope and its risks: the smallest coherent correction, behavior to
   preserve with the cases that rely on it, and what the correction could break
   (other callers, cases relying on current behavior, stored data,
   compatibility) with how the correction avoids each.
5. Agreement on expected behavior and scope.

This document is the developer's whole contract; no other planning documents are
needed. It is ready when the scope is agreed and the evidence supports a bounded,
verifiable correction; an untested guess is not enough. If evidence cannot be
obtained, record what was found and what is missing. If the evidence shows no
change is warranted, agree that with the user and record the conclusion with its
evidence and limits; the flow then completes without a fix. An unavailable
reproduction does not prove there is no defect. When the fix disproves the
cause or changes the scope, update the investigation and reconfirm the changed
decisions.
