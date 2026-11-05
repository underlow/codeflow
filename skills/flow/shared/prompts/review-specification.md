Review `specification.md`, which combines the requirements (the behavioral
contract) and the design (the technical proposal) in one document.

Check scope, ambiguous behavior, failures and later actions, compatibility,
feasibility, component ownership, and shared contracts. Verify consequential
claims against the code. Each material requirement needs a plausible mechanism,
but do not demand private implementation detail. Point out missing user
agreement instead of approving a product choice on the user's behalf.

Check that the component interaction diagram and explanation show how the
behavior works, who owns important state, and what changes at component or data
boundaries. Verify that decisions about affected APIs, storage, compatibility,
permissions, and dependencies are covered in the document. Report unnecessary
layers or mechanisms with a simpler alternative that meets the same requirements.

Derive acceptance examples from the requirements, not from the proposed
mechanism: requirement ID, initial state, actions, expected observations, and
what happens next. Missing expected behavior is a finding, not a place to guess.
Include the proposed examples in your response; if you were given examples from
an earlier review, recheck only those the changes affect.
