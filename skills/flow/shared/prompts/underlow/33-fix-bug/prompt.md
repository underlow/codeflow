Implement the correction described in the current investigation noninteractively.
The investigation owns expected behavior, cause evidence, fix scope, behavior to
preserve, and regression expectations. No separate requirements, design, plan,
or task files are needed. Follow applicable project instructions.

Verify the relevant cause against current code, then make the smallest coherent
fix including affected callers and necessary supporting changes. Preserve unrelated
work. Add a behavior regression test where useful; demonstrate that it catches
the original defect before the fix when feasible, and passes after it. Rerun the
reported reproduction when possible, check affected nearby behavior, and run required
project checks. Record any unavailable environment or unexecuted check explicitly.
Update maintained documentation if the correction changes documented behavior.

When returning from review, verify every selected finding's trigger,
reachability, and consequence. Correct supported findings selected for this
correction, reject unsupported findings with evidence, and retain accepted or
nonblocking findings. Bring a consequential impact disagreement back to the
coordinator. Check all affected paths.
Do not expand product scope or refactor unrelated code.
Return revise-investigation if the cause is disproved, essential behavior is unclear,
or the agreed scope must change. State the new evidence and preserve valid work.
Return blocked if an unavailable prerequisite prevents the crucial correction.
Return done only when the agreed correction, selected findings, and available
required checks are complete. A fixable failing
test is work to complete here, not a reason to declare done.

In the final response, give the corrected behavior, actual reproduction and test
results, review finding dispositions on retries, and remaining limitations.
Commit the fix with a concise message. Do not edit the investigation or original
reviews or launch agents. The next stage reviews the complete current fix.
