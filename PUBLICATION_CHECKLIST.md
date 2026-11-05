# Publication Checklist

Local path: `New project/movacore-portfolio`  
Public GitHub: https://github.com/JuliShestakova/movacore-portfolio (**PUBLIC**, already created)  
Private sources audited read-only: `max_bot`, `nayti_servis`  

Stage 2 documentation and demos are included in the `feat: expand MovaCore engineering portfolio` commit (owner-confirmed push).

## A. Security scan (re-check)

| Check | Result |
|---|---|
| No production `.env` committed | **PASS** — only `examples/.env.example` with placeholders |
| No API keys / tokens / passwords in docs | **PASS** — demo key strings are clearly fake |
| No VPS IPs / SSH configs in portfolio docs | **PASS** — infra docs omit hosts |
| No customer PII / DB dumps / logs | **PASS** |
| No verbatim private commercial source | **PASS** — rewritten demos + docs only |
| No private git history imported | **PASS** — separate portfolio repo |
| Private product repos untouched by this stage | **PASS** — portfolio directory only |
| `.cursor` tooling not published | **PASS** — removed earlier |

## B. Technical honesty

| Claim area | Notes |
|---|---|
| Stack | FastAPI, React/Vite/TS, Flutter, Postgres 16, Redis, RQ, Docker — audit-confirmed |
| AI | Structured LLM + tools + HITL for ads-ops — implemented; mobile AI assistant not claimed shipped |
| Case studies | Five cases from audited behavior; **no invented metrics** |
| About the Builder | Entrepreneur / product builder; no Senior/Lead/Researcher titles |
| License | MIT applies to **this portfolio’s docs & demos only**; private MovaCore code excluded |

## C. Content status

| Artifact | Status |
|---|---|
| README.md | Present; Stage 2 links pending push |
| About the Builder | `docs/about-the-builder.md` |
| Case studies | `docs/case-studies.md` (5 cases) |
| Architecture `.mmd` | Updated diagrams + `architecture/README.md` |
| examples + pytest + CI | Present; run instructions expanded |
| Screenshot shot list | `assets/screenshots/SHOT_LIST.md` |
| Actual screenshot PNGs | **Still needed from owner** (test data only) |
| GitHub public repo | **Done** |
| Stage 2 commit/push | **Done** (owner confirmed) |

## D. Owner follow-ups

1. Capture screenshots per `assets/screenshots/SHOT_LIST.md`.  
2. Optionally refresh GitHub topics/description from `REPO_META.md`.  
3. Do not add real secrets or production `.env` files.

## E. Intentionally hidden

- Private source and commit history  
- Secrets, tokens, supplier credentials  
- Production hostnames / IPs / SSH  
- Tenant PII, real orders/bookings  
- Verbatim commercial pricing algorithms  
