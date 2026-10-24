Review the complete change for the focus described in the supplied aspect file.
Read surrounding callers and consumers, not only the diff.

Take expected behavior from the requirements and acceptance examples, and
binding decisions from the design. Follow each affected user action through its
entry points, inputs, state, errors, and the result the user sees; when a defect
sits in shared logic, check its other uses. When you are given earlier findings,
check them and any newly affected behavior.

Leave out unsupported preferences, unrelated pre-existing problems, and
speculative optimizations.
