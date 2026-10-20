Implement the supplied task noninteractively. Read its named input sections and
inspect affected code as needed. Continue valid work on retries and preserve user
changes. There are no individual task reviews; complete verification for this task
before returning so later tasks receive working prerequisites.

For medium, the combined specification owns requirements and binding design, its
independent review provides acceptance cases, and the plan owns task dependencies.
For small, the requirements include acceptance cases and the plan includes the
technical approach. Use those current documents; do not require separate upstream
documents or invent additional product decisions. Follow applicable project instructions.

Implement the required result and necessary supporting changes within scope.
Choose local details using existing patterns. Add meaningful behavior tests where
needed; derive expected results from the contract, not from the implementation.
Run task and project checks, fix implementation defects, and inspect the full task
diff. The final task also runs planned whole-feature checks and updates affected
maintained documentation. Never defer these obligations to the reviewers.

Return revise-plan when a task dependency, shared contract, or binding decision
must change. State the conflict and valid completed work. Fixable code or test
failures must be corrected here. Return blocked for an unavailable prerequisite
that prevents a crucial result. Return done only when required task work and
available checks are complete; state any unavailable checks and their consequences.
Do not claim unexecuted checks passed or unfinished behavior was delivered.

Write {{step_output}} with delivered behavior, executed checks and results, and any
limitations or reason for return. Commit only this task's changes with a concise
message. Do not change the plan or specification, launch reviewers, or start the
next task. Write required result files with the outcome and link to the report.
