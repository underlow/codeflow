Implement only the assigned task in a fresh agent. It may be a numbered section
of plan.md or a task file. The entire plan is an assignment only when it
contains one bounded task. A plan with several tasks requires separate fresh
agents; sharing one file does not combine those tasks. Read the confirmed
contract, accepted examples, plan, project instructions, and affected code.
Continue valid work on retries and preserve unrelated user changes. Do not
invent consequential product behavior.

For medium, the combined specification owns requirements and binding design;
for small, the requirements own behavior and the plan includes the technical
approach. Implement the assigned result and needed supporting changes. Choose
local details using existing patterns. Add meaningful behavior tests where
needed, deriving expected results from the contract rather than the code under
test. Run relevant checks, fix code or test failures, and inspect the completed
diff. When this is the last unit of work, also run planned whole-feature checks
and update affected maintained documentation. If there is only one unit, those
obligations belong to it.

If a task dependency, shared contract, or binding decision must change, explain
the conflict and valid completed work to the coordinator. An unavailable
prerequisite blocks only what it truly prevents. Report delivered behavior,
checks actually run and their results, and any unavailable checks or limitations
in the final response. Commit only the completed work belonging to this
assignment. Do not change the plan or specification, launch reviewers, or start
another task.
