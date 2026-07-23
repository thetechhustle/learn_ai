# Example Diff Review Output

```text
Evidence mode: SIMULATED
Changed paths:
- starter/index.html
- starter/expected/summary.json

Criterion mapping:
- T-104 owner line satisfies the named assignment criterion.
- unassignedOpen 0 satisfies the directly affected expected-summary criterion.

Risk findings:
- No credential, network marker, dependency, real-person data, or unrelated
  path appears in the supplied diff.

Machine evidence:
- Supplied transcript shows the expected stale-summary failure and eight passes
  after correction. I did not execute it.

Human checks remaining:
- Confirm T-104 displays You.
- Confirm combined filters still show only T-105.
- Check keyboard operation and narrow-screen reflow.

Disposition: ACCEPT FOR SIMULATED EXERCISE
Reason: Every supplied line maps to the brief, with live execution and human
browser behavior still unproven.
```
