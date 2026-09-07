#!/usr/bin/env python3
"""Small dependency-free integrity checks for UX Craft."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "skills/ux-craft/SKILL.md",
    "skills/ux-craft/references/principles.md",
    "skills/ux-craft/references/principles.json",
    "skills/ux-craft/references/playbooks.md",
]


def validate() -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")
    catalog = ROOT / "skills/ux-craft/references/principles.json"
    if catalog.is_file():
        try:
            data = json.loads(catalog.read_text(encoding="utf-8"))
            if len(data) != 30:
                errors.append(f"Expected 30 principles, found {len(data)}")
            ids = [item.get("id") for item in data]
            if len(ids) != len(set(ids)):
                errors.append("Principle IDs must be unique")
        except Exception as exc:
            errors.append(f"Invalid principles.json: {exc}")
    skill = ROOT / "skills/ux-craft/SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        for heading in ["## 1. Identify the work", "## 6. Verify against the real task", "## 7. Deliver the result"]:
            if heading not in text:
                errors.append(f"Missing SKILL section: {heading}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("UX Craft validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
