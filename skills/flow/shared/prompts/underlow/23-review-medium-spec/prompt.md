Review the current combined specification for a medium feature. Its purpose and
requirements are the behavioral contract; its design is the technical proposal.
Do not require separate concept, requirements, or design files.

Check scope, ambiguous behavior, failures and later actions, compatibility,
feasibility, component ownership, and shared contracts. Verify consequential
claims against the affected repository code. Each material requirement needs a
plausible mechanism, but do not demand private implementation detail. Identify
missing user agreement rather than approving a product choice on their behalf.

Derive acceptance examples from the requirements, not from the proposed mechanism.
Each proposed example needs a requirement reference, initial state, actions,
expected observations, and important continuations. Missing expected behavior
is a finding, not a place to guess. When the specification has changed since
an earlier review, recheck the examples it proposed. Return proposed examples in
your final response; the coordinator adds accepted ones to the specification.
