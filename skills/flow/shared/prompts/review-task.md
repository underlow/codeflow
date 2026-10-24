Review one task's result before later tasks build on it. Judge the behavior and
shared contracts the task promised, not work assigned to later tasks.

Follow each behavior the task changed through its entry point, inputs, state,
success and failure paths, recovery, and downstream consumers, including other
uses of a faulty shared rule. Check whether the tests would catch plausible
violations, with expectations derived from the contract rather than the
implementation. When you are given earlier findings, check the complete
corrected task and the developer's evidence; do not repeat resolved findings or
demand details the contract leaves open.
