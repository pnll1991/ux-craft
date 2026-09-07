#!/usr/bin/env python3
"""Offline installer for UX Craft."""
from __future__ import annotations
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "ux-craft"
DIRECTORIES = {
    "codex": Path(".agents"),
    "claude": Path(".claude"),
    "cursor": Path(".cursor"),
}


def install(agent: str, project: Path, dry_run: bool = False) -> Path:
    if agent not in DIRECTORIES:
        raise ValueError(f"Unsupported agent: {agent}")
    project = project.expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    destination = project / DIRECTORIES[agent] / "skills" / "ux-craft"
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing installation: {destination}")
    if dry_run:
        return destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description="Install UX Craft into an existing project")
    parser.add_argument("--agent", choices=sorted(DIRECTORIES), required=True)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    destination = install(args.agent, args.project, args.dry_run)
    print(("Would install to " if args.dry_run else "Installed to ") + str(destination))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
