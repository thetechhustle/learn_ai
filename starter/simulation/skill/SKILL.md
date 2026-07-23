# Diff Evidence Review

## Trigger

Use when a proposed starter-project change must be accepted, revised, or
rejected from a supplied diff.

## Required inputs

- The written brief and acceptance criteria.
- A diff limited to the starter project.
- Machine-check output or an explicit statement that it is unavailable.
- The reviewer's evidence mode: live or simulated.

## Procedure

1. List every changed path.
2. Map each changed line to one acceptance criterion.
3. Flag any credential, network marker, real-person data, dependency, or
   unrelated path.
4. Compare actual and expected verification results.
5. Name human checks that remain.
6. Stop and request clarification if a line has no criterion or provenance.
7. Return exactly one disposition: ACCEPT, REVISE, or REJECT.

## Output contract

```text
Evidence mode:
Changed paths:
Criterion mapping:
Risk findings:
Machine evidence:
Human checks remaining:
Disposition:
Reason:
```

Do not edit files, run commands, connect tools, or infer a passing check that
was not supplied.
