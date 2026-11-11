Implement the correction described in `problem.md`, which defines the
expected behavior, cause, correction scope, behavior to preserve, and
regression expectations.

Inspect the affected code and existing mechanisms to confirm the cause and
understand where the correction belongs. Then make the smallest coherent fix,
including affected callers. Turn the recorded reproduction into a regression
test where useful and show that it fails before the fix when feasible. Rerun
the reproduction when possible and check the behavior the problem document says to
preserve. Do not expand scope or refactor unrelated code.

If the cause is disproved, the expected behavior is unclear, or the scope must
change, explain the issue and the decision needed to the coordinator. Do not
edit `problem.md`.
