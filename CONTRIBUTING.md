# Contributing

Improve an actual task, not the number of rules in the repository. Contributions in English or Spanish are welcome.

## A useful change

Describe the observed problem and the user task it affects. Provide a small reproduction, the proposed implementation or instruction change, its trade-off and a verification step. Label hypothetical examples clearly. Never attach credentials, customer records or private screenshots.

When editing a principle, update both `skills/ux-craft/references/principles.json` and its Markdown card. The validator checks that their content stays aligned. Keep all source URLs and distinguish a source’s claim from your own recommendation. Do not copy posters, source paragraphs or branded artwork. Add a source to the review ledger only after inspecting it.

Keep `SKILL.md` focused. Add task-specific depth to references rather than turning the entry point into a textbook. Preserve progressive loading, user-language behavior and explicit audit-versus-edit boundaries.

## Checks before a pull request

Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. For demo changes, follow the optional browser checks in [evaluation](docs/EVALUATION.md), inspect narrow and wide layouts, keyboard navigation and reduced motion, and update screenshots only from the actual demo.

New files intended for a release must be deliberately added to `release-files.json`. Do not regenerate it from an unreviewed working directory. Never include `.env` files, tokens, personal data, vendor caches or `.git` history. The publisher only copies declared files.

Explain tests actually run and those not run. For instruction changes, include at least one relevant behavioral scenario; do not claim an evaluation passed merely because a text linter passed.

## Review expectations

Accessibility and truthful task completion take priority over decorative novelty. Preserve the original material’s MIT license and third-party attribution. Changes that add fabricated proof, dark patterns, secret collection, automatic publication or unnecessary dependencies are out of scope.
