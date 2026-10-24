Implement the correction described in the current investigation. The
investigation owns expected behavior, cause evidence, fix scope, behavior to
preserve, and regression expectations. No separate requirements, design, plan,
or task files are needed.

Verify the relevant cause against current code, then make the smallest coherent
fix including affected callers and necessary supporting changes. Add a behavior
regression test where useful; demonstrate that it catches the original defect
before the fix when feasible, and passes after it. Rerun the reported
reproduction when possible, check affected nearby behavior, and run required
project checks. Record any unavailable environment or unexecuted check
explicitly. Update maintained documentation if the correction changes documented
behavior. Do not expand product scope or refactor unrelated code.

Report `needs-decision` if the cause is disproved, essential expected behavior is
unclear, or the agreed scope must change; state the new evidence. Report `done`
only when the agreed correction, any selected findings, and available required
checks are complete.

Do not edit the investigation. The coordinator chooses review of the complete
current fix.
