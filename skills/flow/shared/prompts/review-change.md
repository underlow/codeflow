Review the complete change for the focus described in the supplied aspect files.
Read surrounding callers and consumers, not only the diff.

Check whether the implementation reveals a problem with the approach itself,
including local fixes that leave a shared architectural cause intact. Conformance
to the design does not rule out a finding about the approach.

Take expected behavior and binding decisions from the contract named in your
assignment. Follow each affected user action through its
entry points, inputs, state, errors, and the result the user sees; when a defect
sits in shared logic, check its other uses. When you are given earlier findings,
check them and any newly affected behavior.

Leave out unsupported preferences, unrelated pre-existing problems, and
speculative optimizations.
