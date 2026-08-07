# Course Maintenance

This course includes commands, product behavior, package pins, plan details, and
hosting guidance that change outside this repository. A quarterly audit keeps those
claims reviewable without pretending an offline script can prove current facts.

## Ownership and cadence

The **course maintainer** owns the quarterly audit. Each fact record has an
explicit due date on the next quarter boundary: January 1, April 1, July 1, or
October 1. The scheduled run occurs on that boundary and fails until a maintainer
completes and records a new source review. Also review before a release after a
long gap. A second reviewer should approve changes to learner-facing safety
guidance, executable commands, authentication, billing, or production deployment.

GitHub Actions schedules the audit quarterly and also supports manual dispatch.
Locally, run:

```console
$ make audit
$ make audit-test
```

The audit has two deliberately separate outputs:

1. **Static findings** fail on known stale commands and risky runnable patterns.
   These checks are deterministic and offline.
2. **External fact review records** show the last review date, explicit next
   quarter due date, review question, primary source links, and a durable evidence
   record. Missing anchors and due reviews fail the audit. A non-due item is
   labeled `REVIEW RECORDED / NOT REVERIFIED OFFLINE`, never `PASS current`.
   The script does not open a source, confirm that a reviewer opened it, or prove
   that a claim remains accurate.

Use `python3 scripts/audit_course.py --as-of YYYY-MM-DD` to reproduce a dated run.

The Chapter 12 [certification source log](certification-source-log.md) uses the same discipline for provider eligibility, exam-format, video, SDK, and MCP claims. Recheck it before a cohort, workshop, paid exam decision, or derivative video is published.

CI uploads `content-audit-report.json` as the evidence artifact even when a check
fails.

## Quarterly procedure

1. Run `make audit-test`, then `make audit`.
2. Resolve each static finding by checking the current primary documentation and
   updating the lesson, examples, and learner recovery guidance together.
3. For every due external fact, open each primary source and capture the relevant
   product version, page title, and access date in a pull request or issue.
4. Exercise runnable commands in a disposable test project with test credentials.
   Check success, expected failure, and a learner recovery path.
5. Update that fact's `last_reviewed`, `review_due`, and `evidence_record` values
   in `scripts/audit_course.py`. Set `review_due` to the next January 1, April 1,
   July 1, or October 1 scheduled run. Link `evidence_record` to the merged pull
   request, issue, or commit containing the source review. Change the anchor only
   when the learner-facing claim changed too.
6. Run `make audit`, `make build`, and inspect the diff. Have the second reviewer
   confirm high-impact changes before merge.

The linked pull request, issue, or commit is the durable evidence record. It
should identify the fact IDs, primary sources, access dates, commands tested,
environment, results, and any follow-up issue. A CI artifact alone is not durable
review evidence because artifact retention is limited. Do not paste credentials,
private account data, or provider invoices into evidence.

## Updating pinned tools

A version pin is reviewed executable code, not routine prose maintenance. For each
pin:

1. Confirm the package's official publisher and registry provenance.
2. Read release notes and the diff from the current version, including transitive
   dependency or tool-surface changes.
3. Run it in a disposable, least-privilege environment against synthetic data.
4. Inventory new or changed tools, permissions, network access, and external side
   effects.
5. Update the command, its nearby reviewed-date statement, and the matching
   `ExternalFact` entry in the audit script in one pull request.
6. Record exact old/new versions and test evidence in the pull request.

Do not replace a reviewed pin with `@latest`, an unbounded version range, or an
installer copied from an unofficial source.

## Audit exceptions

Exceptions exist for accurate instructional examples that a broad static rule
cannot distinguish safely. They are not a way to silence an inconvenient failure.
Place an `allow-next` HTML comment immediately before the one matching line. It
must include the printed rule ID, accountable owner, expiration date, and concrete
reason, using this shape:

```text
course-audit: allow-next RULE_ID owner="Named owner" review-by="YYYY-MM-DD" reason="Why learners must see this exact example"
```

Wrap that text in an HTML comment when applying it. The next matching line consumes
the exception. Unknown, unused, duplicate, and expired exceptions fail the audit.
Keep the review date within one quarter. The pull request must explain why a safer
example would be less accurate, and a second reviewer must approve it.

Never create exceptions for leaked credentials, unreviewed moving dependencies, or
a convenience-only destructive command. Fix those findings.

## Changing the audit

Static rules favor high-confidence, learner-visible problems over broad heuristics.
They scan the site source, workflow files, root README, and starter README. Lesson
files must begin their heading structure with one H1; MkDocs must not infer a page
title above a source-level H3.
When adding a rule:

- Give it a stable ID and an actionable replacement.
- Add positive, exception, and expiration coverage to `--self-test`.
- Test it against the whole repository and investigate every match.
- Avoid auto-fixes. Context determines whether a command should be replaced,
  removed, or reframed as a warning.

When a product changes unexpectedly between quarterly runs, update the material
immediately and add or refine a rule if the obsolete form could recur.
