# Mock Permission Decisions

Write a decision and reason before revealing each supplied disposition.

## Prompt A

```text
Read starter/index.html, starter/expected/summary.json, and starter/verify.js.
```

**Supplied disposition:** Approve. The files are local, synthetic, and directly
necessary. Reading is lower impact, though the learner must still confirm the
paths contain no sensitive data.

## Prompt B

```text
Write the named owner and expected-summary lines in starter/index.html and
starter/expected/summary.json.
```

**Supplied disposition:** Approve once. The scope matches the brief and has a
path-specific recovery plan.

## Prompt C

```text
Run curl with the project files to get an external quality score.
```

**Supplied disposition:** Deny. The brief prohibits network transfer, no
destination or data policy is established, and the action is unnecessary.

## Prompt D

```text
Delete the starter folder and regenerate it to ensure consistency.
```

**Supplied disposition:** Deny. This is destructive, disproportionate, and
would erase useful evidence. Repair the two named lines instead.

## Prompt E

```text
Read $HOME/.ssh and the parent Downloads folder to look for related context.
```

**Supplied disposition:** Deny. The paths are outside the intended workspace
and are unnecessary. A project folder alone would not technically prevent this
access; permission and sandbox policy must.
