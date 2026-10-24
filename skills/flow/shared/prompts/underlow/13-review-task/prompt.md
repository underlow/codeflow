Review the supplied task's result before dependent work uses it. Inspect its
contract, commits, uncommitted changes, surrounding code, and actual
validation evidence. Judge the task's promised behavior and shared contracts,
not work deliberately assigned to later tasks.

Check each changed or task-owned behavior through its entry point, inputs,
preconditions, state, validation, success and failure paths, cleanup or recovery,
downstream consumers, and observable result. Include alternative supported
paths and other uses of a defective shared rule. Check whether tests would catch
plausible violations using expected behavior established independently of the
implementation. When tests changed or their claims matter to the task, also
apply the supplied test-quality aspect. Run a focused safe check only to resolve a material
doubt. Finish the assigned scope after finding an early defect.

When your assignment includes earlier findings and their corrections, inspect
the complete corrected task and any newly affected behavior, and check the
fixer's evidence. Do not repeat resolved
findings or demand implementation details that the agreed contract leaves open.
Report credible behavioral, contract, or meaningful verification problems with
trigger, evidence, consequence, and uncertainty.
