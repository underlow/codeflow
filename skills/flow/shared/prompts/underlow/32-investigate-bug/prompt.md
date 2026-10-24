Investigate the reported bug and clarify the intended behavior with the user.
Inspect affected code, tests, logs, and configuration. Attempt a focused reproduction
or a disposable probe without changing application code. Trace the trigger through
the actual path to its cause. Separate observed evidence from hypotheses. If the
original environment is unavailable, record what was tested locally and what
remains unverified; never claim a reproduction that did not run.

Write one investigation in investigation.md:
1. Original report and source, expected versus actual behavior, affected scope.
2. Reproduction: prerequisites, inputs or actions, observed results, and limitations.
3. Cause: supporting code or runtime evidence, affected nearby paths, and remaining
   hypotheses. State why the proposed correction addresses the cause.
4. Fix scope and regression expectations: smallest coherent correction, behavior
   to preserve, checks and expected observations for the reported and nearby cases.
5. Agreement on expected behavior and correction scope.

This document is the developer's complete contract. Do not create separate concept,
requirements, design, plan, or task files. Resolve ambiguity in expected behavior
and consequential scope changes with the user. When the fix disproves the cause
or shows the scope must change, incorporate the new evidence and reconfirm
changed consequential decisions.
The investigation is ready only with an agreed scope and enough evidence to
implement and verify a bounded correction; an untested guess is insufficient.
If essential evidence cannot be obtained, preserve the findings in
investigation.md and explain what is missing. Do not modify production data or
application code during investigation.
