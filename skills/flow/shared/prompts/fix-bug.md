Implement the correction described in `investigation.md`, which defines the
expected behavior, cause, fix scope, behavior to preserve, and regression
expectations.

Confirm the cause in the current code, then make the smallest coherent fix,
including affected callers. Add a regression test where useful and show that it
fails before the fix when feasible. Rerun the reported reproduction when possible
and check nearby behavior. Do not expand scope or refactor unrelated code.

Report `needs-decision` if the cause is disproved, the expected behavior is
unclear, or the scope must change. Do not edit the investigation.
