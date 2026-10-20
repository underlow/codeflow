Review whether the agreed design can satisfy the reviewed requirements and give
a developer enough direction without inventing consequential architecture.
Check the whole affected design, even after finding one defect.

Trace important requirements and acceptance cases through the participating
components. Check actual entry points, changes from the existing system, state
ownership and lifetime, shared contracts, and data or event flow through success,
failure, cancellation, recovery, and later use. Verify claims about existing
components in the repository. A restatement of requirements without a component
or mechanism responsible for each consequential behavior is not a design.

Check that the design neither narrows nor silently changes the required behavior.
Report missing mechanisms, incompatible contracts, or ownership gaps that would
force planning to make a consequential decision. If a shared mechanism is
problematic, inspect the other behaviors that depend on it. An unresolved product
choice belongs back with the user through requirements. Do not demand line
numbers, exhaustive file inventories, private signatures, task order, or test
bodies. Routine local engineering choices can remain open.
For a new or changed shared module boundary, check whether it hides meaningful
complexity from callers or merely adds a pass-through layer. Raise this only when
the boundary creates a concrete maintenance or integration cost.

Follow the common review contract. Return concrete findings and limitations in
the final response. Do not edit the design or code, commit, or launch agents.
