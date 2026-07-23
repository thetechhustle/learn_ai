#!/usr/bin/env python3
"""Offline, deterministic checks for stale course commands and reviewable facts."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Rule:
    rule_id: str
    pattern: str
    message: str
    replacement: str
    flags: int = 0


@dataclass(frozen=True)
class ExternalFact:
    fact_id: str
    path: str
    anchor: str
    last_reviewed: str
    review_every_days: int
    owner: str
    evidence: tuple[str, ...]
    question: str


@dataclass(frozen=True)
class Finding:
    rule_id: str
    path: str
    line: int
    message: str
    replacement: str


@dataclass(frozen=True)
class ExceptionUse:
    rule_id: str
    path: str
    line: int
    owner: str
    review_by: str
    reason: str


@dataclass(frozen=True)
class FactStatus:
    fact_id: str
    path: str
    status: str
    last_reviewed: str
    review_due: str
    owner: str
    question: str
    evidence: tuple[str, ...]


RULES = (
    Rule(
        "STALE_COST_COMMAND",
        r"(?<![\w/])/cost(?![\w/])",
        "`/cost` is not the current usage command.",
        "Use `/usage` and distinguish subscription allowance from API billing.",
    ),
    Rule(
        "STALE_REWIND_COMMAND",
        r"(?<![\w/])/rewind(?![\w/])",
        "`/rewind` is not the current checkpoint interaction.",
        "Describe double Escape at an empty prompt and verify the current docs.",
    ),
    Rule(
        "STALE_NODE_18",
        r"\bNode(?:\.js)?(?:\s+version)?\s+18\b",
        "Node 18 guidance is stale for the current npm Claude Code package.",
        "Prefer the native installer; if documenting npm, verify its current requirement.",
        re.IGNORECASE,
    ),
    Rule(
        "MOVING_NPX_LATEST",
        r"^\s*(?:[$>]\s*|run:\s*)?npx\b[^\n]*@latest(?:\s|$)",
        "A runnable `npx ...@latest` example executes an unreviewed moving target.",
        "Pin a reviewed version and document its provenance and update procedure.",
        re.IGNORECASE,
    ),
    Rule(
        "MCP_OPTION_ORDER",
        r"^\s*(?:[$>]\s*|run:\s*)?claude\s+mcp\s+add\s+(?!-)\S+\s+"
        r"(?:(?!--(?:\s|$)).)*(?:--env|-e)(?:\s|=)",
        "Claude MCP options are shown after the server name.",
        "Put Claude options before the server name and `--` before the server command.",
        re.IGNORECASE,
    ),
    Rule(
        "GIT_ADD_ALL",
        r"^\s*(?:[$>]\s*|run:\s*)?git\s+add\s+\.\s*$",
        "Blanket staging can hide unrelated or sensitive changes.",
        "Stage reviewed paths explicitly.",
        re.IGNORECASE,
    ),
    Rule(
        "GIT_RESTORE_ALL",
        r"^\s*(?:[$>]\s*|run:\s*)?git\s+(?:restore|checkout)\s+\.\s*$",
        "Blanket restore can discard unrelated work.",
        "Inspect the diff and restore only named tracked paths.",
        re.IGNORECASE,
    ),
    Rule(
        "GIT_RESET_HARD",
        r"^\s*(?:[$>]\s*|run:\s*)?git\s+reset\s+--hard(?:\s+\S+)?\s*$",
        "Hard reset is destructive and can discard tracked work.",
        "Teach a reviewed checkpoint workflow with explicit scope.",
        re.IGNORECASE,
    ),
    Rule(
        "GIT_CLEAN_DELETE",
        r"^\s*(?:[$>]\s*|run:\s*)?git\s+clean\s+-[a-z]*f[a-z]*"
        r"(?:\s+\S+)*\s*$",
        "Forced Git clean deletes untracked files.",
        "Use `git clean -nd` only as a preview and remove confirmed paths explicitly.",
        re.IGNORECASE,
    ),
    Rule(
        "GIT_FORCE_PUSH",
        r"^\s*(?:[$>]\s*|run:\s*)?git\s+push\b[^\n]*\s--force(?:\s|$)",
        "A runnable force-push example can overwrite shared history.",
        "Avoid it in learner commands; document exceptional recovery separately.",
        re.IGNORECASE,
    ),
    Rule(
        "SKIP_PERMISSIONS",
        r"^\s*(?:[$>]\s*|run:\s*)?claude\b[^\n]*--dangerously-skip-permissions",
        "This command bypasses the normal permission gate.",
        "Teach scoped permissions and sandboxing instead.",
        re.IGNORECASE,
    ),
    Rule(
        "WORLD_WRITABLE",
        r"^\s*(?:[$>]\s*|run:\s*)?chmod\s+(?:-R\s+)?777\b",
        "World-writable permissions are an unsafe learner default.",
        "Use the minimum owner/group permissions required.",
        re.IGNORECASE,
    ),
)


EXTERNAL_FACTS = (
    ExternalFact(
        "CLAUDE_CODE_SETUP",
        "docs/course/setup.md",
        "recommends the native installer",
        "2026-07-23",
        92,
        "Course maintainer",
        ("https://code.claude.com/docs/en/setup",),
        "Are the recommended installers, supported platforms, account access, and npm "
        "fallback requirements still accurate?",
    ),
    ExternalFact(
        "CLAUDE_CODE_USAGE",
        "docs/course/setup.md",
        "Use `/usage`",
        "2026-07-23",
        92,
        "Course maintainer",
        (
            "https://code.claude.com/docs/en/costs",
            "https://console.anthropic.com/settings/usage",
        ),
        "Does `/usage` still behave as described for subscriptions and API-backed use?",
    ),
    ExternalFact(
        "CLAUDE_CODE_CHECKPOINTS",
        "docs/lessons/06_everyday_workflows/6.1_the_daily_drivers.md",
        "++esc+esc++ at an empty prompt",
        "2026-07-23",
        92,
        "Course maintainer",
        ("https://code.claude.com/docs/en/interactive-mode",),
        "Does the current checkpoint/rewind interaction still use double Escape?",
    ),
    ExternalFact(
        "MCP_AND_PLAYWRIGHT_PIN",
        "docs/lessons/08_mcp_connecting_tools/8.3_connecting_your_first_server.md",
        "@playwright/mcp@0.0.78",
        "2026-07-23",
        92,
        "Course maintainer",
        (
            "https://code.claude.com/docs/en/mcp",
            "https://www.npmjs.com/package/@playwright/mcp",
            "https://github.com/microsoft/playwright-mcp/releases",
        ),
        "Is the MCP CLI syntax still valid, and is the pinned Playwright MCP release "
        "still the version we have reviewed and tested?",
    ),
    ExternalFact(
        "HOSTING_PLAN_TERMS",
        "docs/lessons/11_ship_and_sell/11.1_launch_beyond_github_pages.md",
        "Free-plan terms, quotas, data handling",
        "2026-07-23",
        92,
        "Course maintainer",
        (
            "https://vercel.com/docs/limits",
            "https://docs.netlify.com/manage/accounts-and-billing/billing/",
            "https://developers.cloudflare.com/workers/platform/limits/",
        ),
        "Do the named hosting platforms' current terms support every pricing, quota, "
        "data-handling, and commercial-use claim in the lesson?",
    ),
)


EXCEPTION_RE = re.compile(
    r'^\s*<!--\s*course-audit:\s*allow-next\s+(?P<rule>[A-Z0-9_]+)\s+'
    r'owner="(?P<owner>[^"]+)"\s+review-by="(?P<review_by>\d{4}-\d{2}-\d{2})"\s+'
    r'reason="(?P<reason>[^"]+)"\s*-->\s*$'
)


def course_files(root: Path) -> Iterable[Path]:
    candidates = [root / "README.md", root / "mkdocs.yml"]
    candidates.extend(sorted((root / "docs").rglob("*.md")))
    workflows = root / ".github" / "workflows"
    if workflows.exists():
        candidates.extend(sorted(workflows.glob("*.yml")))
        candidates.extend(sorted(workflows.glob("*.yaml")))
    return (path for path in candidates if path.is_file())


def scan_file(
    root: Path, path: Path, as_of: date
) -> tuple[list[Finding], list[ExceptionUse]]:
    findings: list[Finding] = []
    exceptions: list[ExceptionUse] = []
    pending: dict[str, tuple[str, date, str, int]] = {}
    relative = path.relative_to(root).as_posix()

    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        marker = EXCEPTION_RE.match(line)
        if marker:
            rule_id = marker.group("rule")
            if rule_id not in {rule.rule_id for rule in RULES}:
                findings.append(
                    Finding(
                        "INVALID_EXCEPTION",
                        relative,
                        line_number,
                        f"Exception names unknown rule `{rule_id}`.",
                        "Use a rule ID printed by this audit.",
                    )
                )
                continue
            if rule_id in pending:
                findings.append(
                    Finding(
                        "INVALID_EXCEPTION",
                        relative,
                        line_number,
                        f"A prior `{rule_id}` exception has not been consumed.",
                        "Place each allow-next marker immediately before its finding.",
                    )
                )
                continue
            pending[rule_id] = (
                marker.group("owner"),
                date.fromisoformat(marker.group("review_by")),
                marker.group("reason"),
                line_number,
            )
            continue

        matched_rules = {
            rule.rule_id
            for rule in RULES
            if re.search(rule.pattern, line, rule.flags)
        }
        for rule in RULES:
            if rule.rule_id not in matched_rules:
                continue
            if rule.rule_id in pending:
                owner, review_by, reason, _ = pending.pop(rule.rule_id)
                if review_by < as_of:
                    findings.append(
                        Finding(
                            "EXPIRED_EXCEPTION",
                            relative,
                            line_number,
                            f"Exception for `{rule.rule_id}` expired {review_by.isoformat()}.",
                            "Remove the pattern or renew the exception after human review.",
                        )
                    )
                else:
                    exceptions.append(
                        ExceptionUse(
                            rule.rule_id,
                            relative,
                            line_number,
                            owner,
                            review_by.isoformat(),
                            reason,
                        )
                    )
                continue
            findings.append(
                Finding(
                    rule.rule_id,
                    relative,
                    line_number,
                    rule.message,
                    rule.replacement,
                )
            )

        if line.strip() and not re.match(r"^\s*(?:```|~~~)", line):
            for rule_id in set(pending) - matched_rules:
                _, _, _, marker_line = pending.pop(rule_id)
                findings.append(
                    Finding(
                        "MISPLACED_EXCEPTION",
                        relative,
                        marker_line,
                        f"Exception for `{rule_id}` is not immediately before its finding.",
                        "Move it before the matching line; only blank and fence lines may intervene.",
                    )
                )

    for rule_id, (_, _, _, marker_line) in pending.items():
        findings.append(
            Finding(
                "UNUSED_EXCEPTION",
                relative,
                marker_line,
                f"Exception for `{rule_id}` did not precede a matching finding.",
                "Remove the marker or move it directly before the intended example.",
            )
        )
    return findings, exceptions


def check_facts(root: Path, as_of: date) -> list[FactStatus]:
    statuses: list[FactStatus] = []
    for fact in EXTERNAL_FACTS:
        path = root / fact.path
        last_reviewed = date.fromisoformat(fact.last_reviewed)
        review_due = last_reviewed + timedelta(days=fact.review_every_days)
        if not path.is_file() or fact.anchor not in path.read_text(encoding="utf-8"):
            status = "missing-anchor"
        elif as_of >= review_due:
            status = "review-due"
        else:
            status = "current"
        statuses.append(
            FactStatus(
                fact.fact_id,
                fact.path,
                status,
                last_reviewed.isoformat(),
                review_due.isoformat(),
                fact.owner,
                fact.question,
                fact.evidence,
            )
        )
    return statuses


def audit(root: Path, as_of: date) -> dict[str, object]:
    findings: list[Finding] = []
    exceptions: list[ExceptionUse] = []
    files = list(course_files(root))
    for path in files:
        file_findings, file_exceptions = scan_file(root, path, as_of)
        findings.extend(file_findings)
        exceptions.extend(file_exceptions)
    facts = check_facts(root, as_of)
    return {
        "schema_version": 1,
        "as_of": as_of.isoformat(),
        "root": ".",
        "files_scanned": len(files),
        "findings": [asdict(item) for item in findings],
        "exceptions": [asdict(item) for item in exceptions],
        "external_facts": [asdict(item) for item in facts],
        "passed": not findings
        and all(item.status == "current" for item in facts),
    }


def print_report(report: dict[str, object]) -> None:
    findings = report["findings"]
    facts = report["external_facts"]
    exceptions = report["exceptions"]
    print(f"Course content audit as of {report['as_of']}")
    print(f"Scanned {report['files_scanned']} files offline.")
    print()

    print("Static findings")
    if not findings:
        print("  PASS: no stale known commands or risky runnable patterns found.")
    for finding in findings:
        print(
            f"  FAIL {finding['rule_id']} {finding['path']}:{finding['line']}: "
            f"{finding['message']}"
        )
        print(f"       Recommendation: {finding['replacement']}")
    print()

    print("External facts (human verification; no network requests were made)")
    for fact in facts:
        label = "PASS" if fact["status"] == "current" else "REVIEW"
        print(
            f"  {label} {fact['fact_id']}: {fact['status']}; "
            f"reviewed {fact['last_reviewed']}; due {fact['review_due']}"
        )
        print(f"       {fact['question']}")
        for source in fact["evidence"]:
            print(f"       Evidence: {source}")
    print()

    print("Active exceptions")
    if not exceptions:
        print("  None.")
    for item in exceptions:
        print(
            f"  {item['rule_id']} {item['path']}:{item['line']}; "
            f"owner={item['owner']}; review-by={item['review_by']}"
        )

    print()
    print("PASS" if report["passed"] else "FAIL")


def run_self_test() -> int:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "docs").mkdir()
        fact_anchors: dict[str, list[str]] = {}
        for fact in EXTERNAL_FACTS:
            fact_anchors.setdefault(fact.path, []).append(fact.anchor)
        for relative_path, anchors in fact_anchors.items():
            fact_path = root / relative_path
            fact_path.parent.mkdir(parents=True, exist_ok=True)
            fact_path.write_text(
                "# Fixture\n\n" + "\n".join(anchors) + "\n", encoding="utf-8"
            )
        (root / "README.md").write_text(
            "# Test\n\n$ git add .\n\nUse `/cost` here.\n", encoding="utf-8"
        )
        bad = audit(root, date(2026, 7, 23))
        found_ids = {item["rule_id"] for item in bad["findings"]}
        if found_ids != {"GIT_ADD_ALL", "STALE_COST_COMMAND"}:
            print(f"self-test failed: unexpected rules {sorted(found_ids)}", file=sys.stderr)
            return 1
        if {item["status"] for item in bad["external_facts"]} != {"current"}:
            print("self-test failed: current facts were not accepted", file=sys.stderr)
            return 1

        due = audit(root, date(2026, 10, 23))
        if {item["status"] for item in due["external_facts"]} != {"review-due"}:
            print("self-test failed: due facts were not reported", file=sys.stderr)
            return 1

        rule_examples = {
            "STALE_COST_COMMAND": "Use `/cost` here.",
            "STALE_REWIND_COMMAND": "Run `/rewind` now.",
            "STALE_NODE_18": "Install Node.js 18.",
            "MOVING_NPX_LATEST": "$ npx --yes @scope/tool@latest",
            "MCP_OPTION_ORDER": "$ claude mcp add mydb --env DB_URL=x -- npx server",
            "GIT_ADD_ALL": "$ git add .",
            "GIT_RESTORE_ALL": "$ git restore .",
            "GIT_RESET_HARD": "$ git reset --hard HEAD~1",
            "GIT_CLEAN_DELETE": "$ git clean -fd build/",
            "GIT_FORCE_PUSH": "$ git push origin main --force",
            "SKIP_PERMISSIONS": "$ claude --dangerously-skip-permissions",
            "WORLD_WRITABLE": "$ chmod -R 777 uploads",
        }
        for expected_rule, example in rule_examples.items():
            (root / "README.md").write_text(example + "\n", encoding="utf-8")
            example_findings, _ = scan_file(
                root, root / "README.md", date(2026, 7, 23)
            )
            actual_rules = [item.rule_id for item in example_findings]
            if actual_rules != [expected_rule]:
                print(
                    f"self-test failed: {expected_rule} example produced {actual_rules}",
                    file=sys.stderr,
                )
                return 1

        safe_examples = (
            "$ git clean -nd\n"
            "$ git push origin main --force-with-lease\n"
            "$ claude mcp add --env DB_URL=x --transport stdio mydb -- npx server\n"
            "$ claude mcp add mydb -- npx server --env child-option\n"
            "$ npx --yes @scope/tool@1.2.3\n"
        )
        (root / "README.md").write_text(safe_examples, encoding="utf-8")
        safe_findings, _ = scan_file(
            root, root / "README.md", date(2026, 7, 23)
        )
        if safe_findings:
            print(
                "self-test failed: safe examples produced findings "
                f"{[item.rule_id for item in safe_findings]}",
                file=sys.stderr,
            )
            return 1

        (root / "README.md").write_text(
            "# Test\n\n"
            '<!-- course-audit: allow-next GIT_ADD_ALL owner="Test owner" '
            'review-by="2026-08-01" reason="Exception exercise" -->\n'
            "$ git add .\n\nUse `/usage` here.\n",
            encoding="utf-8",
        )
        allowed_findings, allowed_exceptions = scan_file(
            root, root / "README.md", date(2026, 7, 23)
        )
        if allowed_findings or len(allowed_exceptions) != 1:
            print("self-test failed: valid exception was not consumed", file=sys.stderr)
            return 1

        expired_findings, _ = scan_file(
            root, root / "README.md", date(2026, 8, 2)
        )
        if [item.rule_id for item in expired_findings] != ["EXPIRED_EXCEPTION"]:
            print("self-test failed: expired exception was not rejected", file=sys.stderr)
            return 1

        (root / "README.md").write_text(
            '<!-- course-audit: allow-next GIT_ADD_ALL owner="Test owner" '
            'review-by="2026-08-01" reason="Exception exercise" -->\n'
            "This line intervenes.\n"
            "$ git add .\n",
            encoding="utf-8",
        )
        misplaced_findings, _ = scan_file(
            root, root / "README.md", date(2026, 7, 23)
        )
        if [item.rule_id for item in misplaced_findings] != [
            "MISPLACED_EXCEPTION",
            "GIT_ADD_ALL",
        ]:
            print("self-test failed: misplaced exception was not rejected", file=sys.stderr)
            return 1

    print("Course audit self-test: PASS")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (default: inferred from this script).",
    )
    parser.add_argument(
        "--as-of",
        type=date.fromisoformat,
        default=date.today(),
        metavar="YYYY-MM-DD",
        help="Audit date; useful for deterministic tests.",
    )
    parser.add_argument("--json", type=Path, help="Also write the complete JSON report.")
    parser.add_argument(
        "--self-test", action="store_true", help="Run dependency-free internal tests."
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test:
        return run_self_test()
    root = args.root.resolve()
    report = audit(root, args.as_of)
    print_report(report)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
