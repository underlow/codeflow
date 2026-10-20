Review the complete development change for the assigned focus. Use the supplied
base and current commits to inspect all run-owned changes, including uncommitted
work. Distinguish unrelated user changes. Read surrounding callers and consumers
needed to understand behavior, not only the diff. If the boundary is uncertain,
state what you could and could not attribute to this work.

Use the requirements and acceptance examples for expected behavior and the agreed
design for binding technical decisions. Identify affected user actions and code
operations relevant to your focus. Follow each through supported entry paths,
inputs, state, errors, retries, and the result the user sees. When a defect uses
a shared rule or operation, inspect other reachable uses. Complete the assigned
scope before finalizing, even when you find an early defect. On re-review, check
previous findings and newly affected behavior against the complete current scope.

Report credible defects in the change, including a material defect encountered
outside your named focus. Do not defer it merely because another reviewer might
cover that area. Exclude unsupported preferences, unrelated pre-existing
problems, and speculative optimizations. Use the selected aspect guidance for
its particular questions. Follow the common review contract for safe focused
checks, finding evidence, urgency recommendations, and a concise final response.
Do not edit code, tests, planning documents, or Git state, and do not launch
other agents.
