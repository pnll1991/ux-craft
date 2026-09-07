<p align="center"><img src="assets/hero.svg" alt="UX Craft — Less guesswork. Better interfaces. 30 principles, 6 playbooks, 3 modes." width="100%"></p>

<p align="center"><strong>Build with intent. Audit with evidence. Refine without guesswork.</strong></p>
<p align="center">A portable agent skill that turns UX principles into working websites—not a list of laws pasted into a prompt.</p>
<p align="center"><a href="README.es.md">Español</a> · <a href="#start-here">Get started</a> · <a href="docs/index.html">Demo source</a> · <a href="skills/ux-craft/SKILL.md">Read the skill</a> · <a href="LICENSE">MIT license</a></p>

---

## From principle to production decision

**Observed problem → relevant principle → implementation → trade-off → verification.**

That is the unit of work. Not “apply Hick’s law.” Instead: “Organize these plans by the decision people need to make, expose the differences, and test whether they can choose a suitable option.”

UX Craft guides an agent through the actual job: understand the task, map the journey, choose relevant principles, define the visual direction, implement complete states and verify the result. It preserves the project’s stack, brand and explicit constraints.

| Inside | What it is for |
| --- | --- |
| **30 principle cards** | Original apply / avoid / verify notes, each with its source |
| **6 web playbooks** | Service landing, SaaS, commerce, dashboard, forms and content |
| **3 working modes** | Build, audit or refine—without mixing permission boundaries |
| **Accessibility + interaction checks** | Keyboard, forms, responsive layouts, feedback and recovery |
| **Evidence discipline** | No fake metrics, universal “UX score” or invented user research |
| **Portable by design** | Markdown skill; offline installation; no runtime dependencies |

## Start here

From an extracted or cloned copy of this repository, run the installer with **Python 3.10+**. Replace the project path with an existing project directory.

```bash
# Codex
python scripts/install.py --agent codex --project /path/to/your/site

# Claude Code
python scripts/install.py --agent claude --project /path/to/your/site

# Cursor
python scripts/install.py --agent cursor --project /path/to/your/site
```

On Windows, a quoted path such as `"D:\my-site"` works. On systems that expose Python as `python3`, use that command instead.

The installer copies only `skills/ux-craft/`, including its references. It does not download packages, modify agent permissions, collect data or overwrite an existing installation. Preview changes with `--dry-run`. For user-level installation, replace `--project ...` with `--global`.

**No Python?** Copy the entire `skills/ux-craft` folder into the matching skills directory—not just `SKILL.md`.

| Client | Project directory | Explicit use |
| --- | --- | --- |
| Codex | `.agents/skills/ux-craft/` | `$ux-craft` |
| Claude Code | `.claude/skills/ux-craft/` | `/ux-craft` |
| Cursor | `.cursor/skills/ux-craft/` | Select `ux-craft` from the `/` skill menu |
| Other agents | A supported skill directory or attached folder | Explicitly ask the agent to read `SKILL.md` and relevant references |

Paths follow the [official documentation](skills/ux-craft/references/sources.md). Client discovery and model output are not guaranteed by a successful file copy. See [installation details](docs/INSTALLATION.md) and the [QA record](docs/QA.md).

## Give it a real task

```text
Use UX Craft to build this service website.

Preserve the existing stack and brand. Make the offer, scope and next action
clear. Implement the mobile layout and the form’s success, error and recovery
states. Use real content only. Explain the important decisions and test the
core journey. Do not publish it.
```

```text
Use UX Craft to audit this dashboard without modifying files.
Prioritize problems that prevent the main task. For each finding, give the
observed evidence, affected task, proposed change and acceptance check.
Separate observed failures from hypotheses and tests you could not run.
```

[Six ready-to-use prompts →](examples/prompts.md)

The skill, references, templates, demo and default documentation are in English. The agent still responds in the user’s language. [Spanish README](README.es.md) and [Spanish prompts](examples/prompts.es.md) remain available as optional translations.

## See the decisions, not just the decoration

Open **`docs/index.html`** in a browser. The self-contained demo includes a before/after example, a searchable 30-principle library and a local-only form-state exercise. It uses no external fonts, libraries, analytics or network calls. Its example is illustrative—not a customer case or a measured conversion result.

[Annotated landing example](examples/landing-brief-and-decisions.md) · [Evidence-based audit example](examples/audit-example.md)

## What it refuses to pretend

A beautiful interface is not proof of usability. Miller is not a seven-menu-item limit. Fitts does not prescribe one magic pixel size. Doherty is not a Core Web Vitals score. A named principle does not validate a design by itself.

UX Craft rejects fabricated progress, false scarcity, hidden costs and invented testimonials. It treats accessibility, honest feedback and recovery as part of the product—not a final polish pass. [Trade-offs and evidence →](skills/ux-craft/references/conflicts-and-evidence.md)

## A small entry point, useful depth

```text
skills/ux-craft/
├── SKILL.md              # The agent’s working instructions
├── agents/openai.yaml   # Optional Codex display metadata
├── references/          # Principles, playbooks, evidence and checks
├── assets/              # Brief, decision log and audit templates
├── LICENSE
└── NOTICE.md
```

The repository adds the demo, installer, publishing helper, tests and contribution guides. The installed skill contains no executable scripts. Reference material is loaded when needed rather than pushed into every task.

## Verify and contribute

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

These commands need only Python’s standard library. They check package integrity, local links, the source catalog and installer/publisher safeguards. They do **not** measure an agent’s UX quality. The optional browser smoke test and behavioral review scenarios are described in [evaluation](docs/EVALUATION.md).

Contributions should add a reproducible improvement, not another rule without context. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

Created by **Paolo · `pnll1991`**. Inspired by **[Laws of UX](https://lawsofux.com/es/)**, created by **Jon Yablonski**. Independent and unaffiliated.

The review covers the Spanish index’s 30 principle pages and eight articles listed in the article index, reviewed on **2026-09-06**. Application notes, templates, code and artwork are original; source prose and posters are not redistributed. [Review scope and primary references](skills/ux-craft/references/sources.md) · [Notice](NOTICE.md)

**MIT for original project material.** Third-party sources and marks remain with their owners.
