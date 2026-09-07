# Repository instructions

This repository maintains UX Craft, an instruction-only web UX skill. Read `README.md`, `CONTRIBUTING.md` and the specific files being edited before making changes.

Preserve source attribution, original wording, the MIT boundary and English/Spanish README parity. English is the default for the demo, documentation and contribution surfaces; Spanish files are explicitly labeled alternatives. Keep `skills/ux-craft/SKILL.md` concise and move detail into references. Update the JSON principle catalog and Markdown cards together.

Never add fake user research, endorsements, badges, benchmark results or publication claims. Do not copy source-site posters or prose. Do not publish or enable remote services without explicit authorization.

Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. Browser smoke checks are optional and separately documented. Update `release-files.json` deliberately when adding release files; never include credentials, `.git` or unrelated local files. Report tests not run honestly.
