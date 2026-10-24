Investigate the reported bug and agree the intended behavior with the user.
Inspect code, tests, logs, and configuration, and try a focused reproduction or
a disposable probe without changing application code or production data. Trace
the trigger to its cause and separate observation from hypothesis. Never claim a
reproduction that did not run; if the original environment is unavailable, say
what was tested instead.

Write `investigation.md`:

1. Original report and source, expected versus actual behavior, and affected scope.
2. Reproduction: prerequisites, actions, observed results, and limits.
3. Cause: evidence, affected nearby paths, remaining hypotheses, and why the
   proposed correction addresses the cause.
4. Fix scope and regression expectations: the smallest coherent correction,
   behavior to preserve, and checks with expected observations for the reported
   and nearby cases.
5. Agreement on expected behavior and scope.

This document is the developer's whole contract; no other planning documents are
needed. It is ready when the scope is agreed and the evidence supports a bounded,
verifiable correction; an untested guess is not enough. If evidence cannot be
obtained, record what was found and what is missing. When the fix disproves the
cause or changes the scope, update the investigation and reconfirm the changed
decisions.
