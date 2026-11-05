# Live Demo Guide

What reviewers can inspect safely for MovaCore.  
Internal VPS IPs, SSH, admin credentials, and closed endpoints are **not** published here.

## Public product surfaces

| Surface | What you can see | Access |
|---|---|---|
| **MovaCore Parts** storefront | Home, article search, brand disambiguation, supplier offers | Public Unicode domain: `https://гипермаркет-автозапчастей.рф/` (punycode host also resolves). Optional mirror path on the brand site: `https://movacore.ru/s/hypermarket/` |
| **MovaCore Marketing** site | Public marketing landing and product directions | `https://movacore.ru/` |
| **Portfolio demos** | FastAPI + Applied AI teaching examples | This repository (`examples/`) |

Operator cabinets (store `/store/`, service cabinet, platform `/cabinet/`, marketing tools, AI plan apply) require authenticated accounts and are **not** opened as anonymous live demos.

## What works today

- Parts search and offer listing against supplier APIs (server-side)  
- Service discovery and booking flows (web + Flutter against shared API) — **authenticated / app surfaces**; not fully exposed as a separate public anonymous web demo in this guide  
- Marketing cabinet tools + gated ads AI agent (authenticated)  
- Portfolio `examples/` runnable offline with pytest  

## Demo scenarios (safe)

### A. Portfolio API demo (no secrets)

```bash
cd movacore-portfolio
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
source .venv/bin/activate
pip install -r examples/requirements.txt
pytest -q
uvicorn examples.api.demo_app:app --reload --port 8765
```

Open http://127.0.0.1:8765/docs and POST `/demo/v1/parts/search`.

### B. Portfolio Applied AI demos (offline)

```bash
pytest examples/ai -q
```

- Ads-style plan workflow: `examples/ai/agent_workflow.py`  
- Automotive assistant teaching demo: `examples/ai/automotive_assistant.py`  

Uses `EchoLLMClient` — no API key required.  
Live LLM calls need a private `.env` (never commit).

### C. Public Parts storefront browse

1. Open `https://гипермаркет-автозапчастей.рф/`  
2. Search a **demo article** (e.g. `6Q0260849A`) — avoid personal VINs  
3. Select a brand (e.g. VAG) and review offers / analogs UI  

Screenshots from this flow: [`assets/screenshots/parts/`](../assets/screenshots/parts/).

### D. Public Marketing site

Open `https://movacore.ru/` for brand positioning and product directions.  
This is a marketing surface — cabinet login is gated.

### E. Authenticated cabinets (owner-assisted)

Requires a **test account** from the owner:

- Store cabinet for Parts  
- Service cabinet  
- Marketing cabinet + AI plan review  
- Flutter app against staging/LAN  

Not available as anonymous public demo.

## Dependencies for local portfolio demos

- Python 3.11+  
- Packages in `examples/requirements.txt`  
- Optional: LLM key only for live `HttpLLMClient` experiments  

## Closed / not for public demo

- Raw VPS IPs and SSH  
- Production `.env`, supplier keys, ads OAuth tokens  
- Database dumps and customer PII  
- Unauthenticated access to operator cabinets  
- Private GitHub production repositories  

## Related docs

- [AI Demo](ai-demo.md)  
- [Product audit](product-audit-stage3.md)  
- [Screenshot shot list](../assets/screenshots/SHOT_LIST.md)  
