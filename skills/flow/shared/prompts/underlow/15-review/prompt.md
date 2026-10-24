Review the complete development change for the assigned focus. Inspect all
changes of this flow, including uncommitted work. Read surrounding callers and consumers
needed to understand behavior, not only the diff. If the boundary is uncertain,
state what you could and could not attribute to this work.

Use the requirements and acceptance examples for expected behavior and the agreed
design for binding technical decisions. Identify affected user actions and code
operations relevant to your focus. Follow each through supported entry paths,
inputs, state, errors, retries, and the result the user sees. When a defect uses
a shared rule or operation, inspect other reachable uses. Complete the assigned
scope before finalizing, even when you find an early defect. When your
assignment includes earlier findings, check them and newly affected behavior
against the complete current scope.

Report credible defects in the change, including a material defect encountered
outside your named focus. Do not defer it merely because another reviewer might
cover that area. Exclude unsupported preferences, unrelated pre-existing
problems, and speculative optimizations. Use the supplied aspect file for its
particular questions.
