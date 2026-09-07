# Evaluation guide

Package validation and UX evaluation are different jobs.

## Package checks

Run the dependency-free validator and unit tests:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

These checks confirm repository structure and installer behavior. They do not prove the quality of an agent's design output.

## Behavioral evaluation

Give an agent a real task with constraints, then review whether it:

1. identifies the primary user task before selecting principles;
2. preserves the existing stack and explicit requirements;
3. selects only relevant principles;
4. connects each important change to observed evidence and a verification step;
5. implements loading, error, success and recovery states where applicable;
6. avoids fabricated metrics, proof, urgency or research;
7. distinguishes tests actually run from tests not run.

Evaluate at least one Build, Audit and Refine case. Prefer realistic project fixtures over abstract prompts.

## Browser review

For interface changes, inspect narrow and wide layouts, keyboard navigation, visible focus, long content, enlarged text and reduced motion. Exercise one happy path and one failure/recovery path. Screen-reader and performance claims require the corresponding real tools.
