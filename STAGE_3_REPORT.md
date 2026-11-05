# Stage 3 Report — Visual Portfolio & Live Demo

Local work only. **No git push** performed.

## 1. What was checked

- Public Parts storefront (Unicode domain + `movacore.ru/s/hypermarket/` mirror)
- Public Marketing site `https://movacore.ru/`
- Authenticated cabinet entry (`/cabinet/`) — login wall, not captured as “working dashboard”
- Existing portfolio docs / Stage 2 demos
- Read-only product status vs private systems (no private code published)
- `examples/` pytest suite after adding automotive assistant demo
- Lightweight secret pattern scan over portfolio text files

## 2. Applications available (for reviewers)

| Surface | Availability |
|---|---|
| Parts storefront | **Public** — search + offers work with live suppliers |
| Marketing landing | **Public** — brand / product directions |
| Portfolio FastAPI + AI demos | **Local** via `examples/` |
| Store / service / marketing cabinets | **Closed** without test credentials |
| Flutter app | **Closed** without device/staging from owner |
| Dedicated anonymous Service web storefront | **Not confirmed** as a separate public URL in this pass |

## 3. Screenshots obtained

| Path | Notes |
|---|---|
| `assets/screenshots/parts/parts-home.png` | Real home |
| `assets/screenshots/parts/parts-search.png` | Demo article `6Q0260849A` |
| `assets/screenshots/parts/parts-results.png` | Brand picker (9 brands) |
| `assets/screenshots/parts/parts-offer.png` | VAG offers header + tabs |
| `assets/screenshots/marketing/marketing-home.png` | movacore.ru hero |
| `assets/screenshots/marketing/marketing-products.png` | Product directions section |

## 4. Screens unavailable

- Service: discovery list, card, booking web UI  
- Mobile: home, garage, parts, service search, calendar  
- Marketing: live cabinet dashboard, publications queue, AI plan apply UI  
- Parts: authenticated store cabinet  

Folders `service/` and `mobile-app/` contain README placeholders only.

## 5. AI functions that actually work

| Capability | Status |
|---|---|
| Marketing ads agent (structured plan → allowlist → HITL) | **Production pattern** (private product; not opened publicly) |
| Portfolio `examples/ai/agent_workflow.py` | **Works offline** (EchoLLMClient) |
| Portfolio `examples/ai/automotive_assistant.py` | **Works offline** as teaching demo — **not** a shipped in-app mechanic |
| In-app AI Automotive Assistant | **Concept** — do not claim GA |

## 6. Documentation added / updated

| Path | Change |
|---|---|
| `docs/product-audit-stage3.md` | UI honesty audit |
| `docs/live-demo.md` | Public vs closed demos + run steps |
| `docs/ai-demo.md` | Ads agent + automotive teaching demo |
| `docs/engineering-interview.md` | 15 interview questions with MovaCore hooks |
| `assets/screenshots/**` | Structure + captures + shot list |
| `examples/ai/automotive_assistant.py` (+ tests) | Safe Applied AI demo |
| `README.md` | Product links, screenshot gallery, Stage 3 doc links |
| `STAGE_3_REPORT.md` | This report |

## 7. Test results

Run from portfolio root after Stage 3 edits:

```text
pytest -q
11 passed, 46 warnings in 0.80s
```

Warnings are upstream `pytest-asyncio` deprecations on Python 3.14 — not demo failures.

## 8. Security check

- No `.env`, private keys, or `VPS_PASS` strings found in portfolio text via pattern scan  
- No private production source copied into the portfolio  
- Screenshots use demo article; Parts/marketing public pages only  
- Marketing captures may include **illustrative** dashboard mockup art on the landing page (site content), not a live authenticated session  
- Did **not** publish internal VPS IPs, SSH, admin URLs as demos, or customer PII dumps  

## 9. Required from the project owner

1. **Test accounts** (synthetic data only) for: store cabinet, service cabinet, marketing cabinet, platform find-service admin — so remaining screenshots can be taken safely.  
2. **Flutter** emulator/device capture for A1–A5 (or grant staging APK + test login).  
3. Confirm whether a **public Service discovery URL** should be listed; if yes, provide the public hostname only.  
4. Review Parts screenshots for any business phone/address comfort level before push.  
5. Explicit **OK to git push** Stage 3 when ready (not done in this stage).  

## Changed tree (Stage 3 focus)

```text
movacore-portfolio/
├── STAGE_3_REPORT.md
├── README.md
├── docs/
│   ├── product-audit-stage3.md
│   ├── live-demo.md
│   ├── ai-demo.md
│   └── engineering-interview.md
├── assets/screenshots/
│   ├── README.md
│   ├── SHOT_LIST.md
│   ├── parts/*.png
│   ├── marketing/*.png
│   ├── service/README.md
│   └── mobile-app/README.md
└── examples/ai/
    ├── automotive_assistant.py
    └── test_automotive_assistant.py
```
