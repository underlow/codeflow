# Changes needing explicit approval

These changes are hard to undo or affect what lies outside the code. Each one
needs the user's explicit approval of that item, not only of the document that
contains it:

- database schema, migrations, and changes to stored data or on-disk formats;
- external contracts: APIs, message and event formats, CLI arguments, config
  format, environment variables, and anything that breaks compatibility;
- changes to existing behavior the request did not ask for, including defaults
  and removed features;
- authentication, authorization, secrets, cryptography, weakened validation, and
  personal data in logs or telemetry;
- new dependencies, major upgrades, and license changes;
- CI, build, deployment, and feature flag defaults;
- payments, outgoing messages, and paid external calls;
- changed or deleted expectations in existing tests.

Project instructions may add categories or paths.

The contract document lists each such change in a section "Changes needing
approval": what changes, why, the consequence, and how to roll it back. Write
"none" when there are none. Bring each item to the user separately and record
the approval beside it.

A developer who needs such a change that is not approved reports
`needs-decision`. A reviewer reports every such change in the diff that is not
approved as a finding.
