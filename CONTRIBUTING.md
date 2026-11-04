# Contributing

This repository is primarily a personal engineering portfolio for MovaCore.

## What belongs here

- Clarifications to architecture documentation
- Fixes to Mermaid diagrams
- Improvements to safe demonstration examples under `examples/`
- Additional tests for demo code
- Screenshots that use only synthetic / test data

## What does not belong here

- Production secrets or private repository source
- Customer or supplier personal data
- Infrastructure endpoints, IPs, or SSH materials
- Large dumps of commercial business logic

## Development (demo code)

```bash
cd examples
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Pull requests

If you open a PR:

1. Keep changes scoped and documented.
2. Run demo tests locally.
3. Confirm no secrets were added (`PUBLICATION_CHECKLIST.md`).
