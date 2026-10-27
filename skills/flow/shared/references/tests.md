# Tests

An automated test is worth keeping when it checks required behavior or a
contract others rely on, through a public boundary, and a plausible future
change could break it. A regression test for a fixed bug qualifies. Anything
else is checked once by hand and reported, not kept as a test.

Do not write tests that:

- check incidental text: log messages, prompt or documentation wording, UI copy,
  exact error messages. Text is a contract only when another program parses it
  or the requirements fix it verbatim;
- restate the code: constants, defaults, enum values, field-by-field mappings,
  constructors, getters, a function or export being present;
- compute the expected value with the code under test or a copy of its logic;
- check structure instead of behavior: private functions, which class does what,
  mock call order or count, DOM structure, element counts, styles, large
  snapshots;
- mock the unit under test, or mock everything around it so only wiring remains;
- check the language, framework, or a library rather than project code;
- assert that removed code, options, or text no longer exist;
- repeat a case with other values but no distinct failure mode, or exist only to
  cover a line or branch;
- carry large generated fixtures or inline data where a minimal example shows
  the behavior;
- depend on real time, sleeps, network, or test order.

A test that only fails on a harmless implementation change is worse than no
test.
