Judge the engineering quality of the implementation as a whole. Read the change
alongside its callers and nearby implementations. Consider how someone working
in this area would understand, verify and modify it.

- Clarity: do names and control flow explain the operation and its intent?
- Responsibilities and coupling: does each component own a coherent job? Must
  callers know its internals to use it correctly?
- Duplication and reuse: find where the project already solves similar problems.
  Check for independently implemented rules, duplicated state and parallel
  mechanisms, including existing library or platform support.
- Data and state: who owns each value and its transitions? Can the model
  represent inconsistent states that callers must guard against?
- API contracts: are inputs, guarantees, failure modes and required call order
  clear to callers?
- Control flow and failures: trace side effects through branches and early exits.
  Where relevant, check the state left by cancellation, partial failure and retry.
- Complexity: do the layers, abstractions and special cases earn their cost for
  the required behavior, including safety and compatibility guarantees?
- Changeability and verification: for a plausible change to a rule, where would
  edits be needed, which consumers would be affected, and how could it be checked?

Give a brief overall assessment and report the most consequential findings,
including issues outside this checklist. Ground each in actual code and explain
what becomes hard to understand, verify or change. Skip style preferences and
per-item status reports.
