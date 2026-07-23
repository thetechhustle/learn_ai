# Mock First Agent Session

This is a prerecorded teaching fixture, not output from the learner's machine.

```text
LEARNER
Inspect the synthetic starter. Assign T-104 to "You", update only the expected
output affected by that change, and explain verification. Add no packages,
network calls, credentials, or real data. Stop if another production file is
needed.

AGENT - GATHER
I would inspect:
- starter/index.html for the canonical task-data block
- starter/expected/summary.json for the expected aggregate
- starter/verify.js to learn the existing checks

I expect two data lines to change. I do not need a package install or network
connection.

YOUR DECISION 1
Is the proposed read scope necessary and proportionate? Record approve or deny
before continuing.

LEARNER
Approved: those three local synthetic files are relevant and read-only.

AGENT - ACT PROPOSAL
Change T-104 owner from an empty string to "You". First run the existing
verifier with the old expected summary to observe the affected assertion, then
change only unassignedOpen from 1 to 0.

YOUR DECISION 2
Would you approve the two named writes? What would make you stop?

LEARNER
Approved only for starter/index.html and starter/expected/summary.json. Stop if
another file, external action, or credential is requested.

AGENT - VERIFY
After the data edit, the summary check fails: expected unassignedOpen 1 but
received 0. After correcting that expected value, all eight checks pass. The
status-plus-risk filter still returns only T-105.

YOUR DECISION 3
Inspect changes.patch. Does the evidence support acceptance, revision, or
rejection? Record unexplained risks.
```

The learner should not infer from this transcript that a live model always
chooses this scope or that a passing verifier covers usability, security, or
external effects.
