# QA record

Current package: **UX Craft 1.0.1 English Edition**.

The source package was validated locally before publication with content/integrity tests and browser checks across narrow and wide layouts. The public repository should still be treated as a source distribution: agent behavior varies by client and model.

## What this repository can verify

- `SKILL.md` structure and required references exist.
- The machine-readable catalog contains 30 unique principles.
- The offline installer copies the skill without overwriting an existing install.
- The demo is static and has no analytics/runtime dependency.

## What it cannot claim automatically

- WCAG conformance.
- Screen-reader compatibility without actual assistive-technology testing.
- Conversion or revenue improvement.
- Universal usability across products or audiences.
- Identical behavior in every agent client.

Run:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

Record browser/user tests separately from package integrity checks.
