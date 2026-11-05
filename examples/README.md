# Demonstration Code

Safe, rewritten examples that illustrate engineering patterns used in MovaCore.

They are **not** a copy of the private production repository.

## Layout

| Path | Contents |
|---|---|
| `api/` | Minimal FastAPI demo app + tests |
| `python/` | Offer sorting / structured errors |
| `ai/` | LLM abstraction, structured plans, HITL apply |
| `schemas/` | Pydantic models for demo contracts |
| `.env.example` | Placeholder env vars only |
| `requirements.txt` | Demo dependencies |

## Prerequisites

- Python 3.11+ (3.12 recommended; CI uses 3.12)
- `pip` / venv

## Setup

From the **repository root** (`movacore-portfolio/`):

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r examples/requirements.txt
```

macOS / Linux:

```bash
source .venv/bin/activate
pip install -r examples/requirements.txt
```

Optional: copy env placeholders (never commit a real `.env`):

```bash
copy examples\.env.example .env
# or: cp examples/.env.example .env
```

## Run tests

```bash
pytest -q
```

Expected: all demo tests pass (API, sorting, AI workflow).

CI: `.github/workflows/demo-ci.yml` runs the same suite on push/PR.

## Run the demo API locally

```bash
uvicorn examples.api.demo_app:app --reload --port 8765
```

- Health: http://127.0.0.1:8765/demo/v1/health  
- Interactive docs: http://127.0.0.1:8765/docs  

Example search:

```bash
curl -s -X POST http://127.0.0.1:8765/demo/v1/parts/search ^
  -H "Content-Type: application/json" ^
  -d "{\"article\":\"6Q0260849A\",\"brand\":\"VAG\",\"include_analogs\":true}"
```

## Applied AI demos

| Module | What it shows |
|---|---|
| `ai/llm_client.py` | Abstract client + Echo stub + HTTP skeleton with retries |
| `ai/agent_workflow.py` | Structured plan → allowlist → human apply |

Live LLM calls via `HttpLLMClient` refuse `sk-demo*` keys. Use a private `.env` only on your machine.

## What is intentionally not here

- Production handlers from the private repo  
- Real supplier or ads credentials  
- Database dumps  
