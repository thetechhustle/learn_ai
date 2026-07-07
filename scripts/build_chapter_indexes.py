#!/usr/bin/env python3
"""Rebuild the 'Lessons in this chapter' index inside each chapter README.

Scans docs/lessons/*/ for numbered lesson files and rewrites the block
between the lesson-index markers so chapter indexes never drift from the
files on disk.
"""

import re
from pathlib import Path

LESSONS_DIR = Path(__file__).resolve().parent.parent / "docs" / "lessons"
START = "<!-- lesson-index:start -->"
END = "<!-- lesson-index:end -->"


def lesson_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return path.stem


def lesson_sort_key(path: Path):
    match = re.match(r"(\d+)\.(\d+)", path.name)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    return (999, 999)


def build_index(chapter: Path) -> str:
    lessons = sorted(
        (p for p in chapter.glob("*.md") if p.name != "README.md"),
        key=lesson_sort_key,
    )
    lines = ["", "## Lessons in this chapter", ""]
    lines += [f"- [{lesson_title(p)}]({p.name})" for p in lessons]
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    for chapter in sorted(LESSONS_DIR.iterdir()):
        readme = chapter / "README.md"
        if not readme.is_file():
            continue
        text = readme.read_text(encoding="utf-8")
        if START not in text or END not in text:
            continue
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        new = f"{head}{START}\n{build_index(chapter)}\n{END}{tail}"
        if new != text:
            readme.write_text(new, encoding="utf-8")
            print(f"updated {readme.relative_to(LESSONS_DIR.parent.parent)}")


if __name__ == "__main__":
    main()
