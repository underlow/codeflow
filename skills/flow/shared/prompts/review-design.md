Review whether the design can satisfy the requirements and gives a developer
enough direction without inventing consequential architecture.

Trace important requirements and acceptance examples through the components:
entry points, changes from the current system, state ownership and lifetime,
shared contracts, and flows through success, failure, cancellation, recovery,
and later use. Verify claims about existing code. Report missing mechanisms,
incompatible contracts, ownership gaps, and any narrowing or change of required
behavior. When a shared mechanism is faulty, check the behaviors that depend on
it. An unresolved product choice is a question for the user, not a design fix.

Do not demand line numbers, file inventories, private signatures, task order, or
test bodies. Flag a new module boundary only when it adds a concrete maintenance
or integration cost without hiding real complexity.
