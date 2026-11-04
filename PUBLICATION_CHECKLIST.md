# Publication Checklist

Local portfolio path: `New project/movacore-portfolio`  
Private sources audited read-only: `max_bot`, `nayti_servis`  
GitHub create/push: **not performed** (awaiting owner confirmation)

## A. Security scan results

| Check | Result |
|---|---|
| No production `.env` committed | **PASS** — only `examples/.env.example` with placeholders |
| No API keys / tokens / passwords in docs | **PASS** (spot-checked; demo key string is clearly fake) |
| No VPS IPs / SSH configs published | **PASS** — infra docs intentionally omit hosts |
| No customer PII / DB dumps / logs | **PASS** — no dumps; screenshots folder empty pending safe media |
| No verbatim private commercial source tree | **PASS** — rewritten demos only |
| No private git history imported | **PASS** — new directory, no copy of `.git` from private repos |
| Private repo settings untouched | **PASS** — no GitHub setting changes |

## B. Technical honesty

| Claim area | Notes |
|---|---|
| Stack | FastAPI, React/Vite/TS, Flutter, Postgres 16, Redis, RQ, Docker — confirmed by audit |
| AI | Structured LLM + tools + HITL for ads-ops path — confirmed; mobile AI assistant **not** claimed as shipped |
| Mobile features | Per-feature status table in `docs/mobile-app.md` |
| Metrics / SLOs / years of experience | **Not invented** |

## C. Content completeness

| Artifact | Status |
|---|---|
| README.md | Done |
| LICENSE / SECURITY / CONTRIBUTING | Done |
| docs/* including mobile-app | Done |
| architecture/*.mmd | Done |
| examples + pytest + CI workflow | Done |
| Issue templates | Done |
| Screenshots | **Pending** — add safe captures before public launch |
| Git init / GitHub remote | **Pending owner confirmation** |

## D. Pre-publish actions for the owner

1. Review every Markdown file for accidental private details.
2. Add safe screenshots under `assets/screenshots/`.
3. Optionally `git init` in this folder only.
4. Create public GitHub repo `movacore-portfolio` and push **after explicit confirmation**.
5. Apply description + topics from `REPO_META.md`.

## E. Intentionally hidden

- Private source code and commit history
- Secrets, tokens, supplier credentials
- Production hostnames / IPs / SSH
- Tenant data, real orders, real bookings
- Exact internal route maps that would aid abuse
- Commercial pricing algorithms copied verbatim
