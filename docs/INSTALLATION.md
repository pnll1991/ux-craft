# Installation

UX Craft is an instruction-only skill. Installing it copies Markdown/reference files into an agent's project skill directory; it does not add runtime dependencies or telemetry.

## Automated local install

Requires Python 3.10+ and an existing project directory.

```bash
python scripts/install.py --agent codex --project /path/to/site
python scripts/install.py --agent claude --project /path/to/site
python scripts/install.py --agent cursor --project /path/to/site
```

Preview the destination without writing:

```bash
python scripts/install.py --agent codex --project /path/to/site --dry-run
```

The installer refuses to overwrite an existing `ux-craft` directory.

## Manual install

Copy the entire `skills/ux-craft` folder, including `references/`, `assets/`, `LICENSE` and `NOTICE.md`.

Typical project locations:

- Codex: `.agents/skills/ux-craft/`
- Claude Code: `.claude/skills/ux-craft/`
- Cursor: `.cursor/skills/ux-craft/`

Client discovery behavior can change independently of this repository. Consult the relevant vendor documentation when a client does not discover the skill automatically.
