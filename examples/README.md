# Demonstration Code

Safe, rewritten examples that illustrate engineering patterns used in MovaCore.

They are **not** a copy of the private production repository.

## Layout

| Path | Contents |
|---|---|
| `api/` | Minimal FastAPI demo app + tests |
| `python/` | Sorting / error helpers |
| `ai/` | LLM abstraction, structured plans, HITL apply |
| `schemas/` | Pydantic models for demo contracts |
| `.env.example` | Placeholder env vars only |

## Run tests

From the repository root:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r examples/requirements.txt
pytest -q
```

## Live LLM calls

`HttpLLMClient` refuses demo keys. Configure real keys only in a local `.env` that is gitignored — never commit them.
