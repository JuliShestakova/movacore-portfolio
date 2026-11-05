# Engineering Interview Prep — MovaCore

Fifteen questions a technical interviewer may ask the builder of MovaCore.  
Each item lists what is being probed, knowledge to prepare, and a **real MovaCore hook** to discuss.

Answers are **not** scripted here — the owner should explain from first-hand experience. Places marked **[owner]** need her own wording, trade-offs, and war stories.

---

## 1. Architecture

**Q:** How is MovaCore structured as a multi-product platform rather than four separate apps?

- **Checks:** system boundaries, shared core vs product surfaces, coupling  
- **Knowledge:** modular monolith vs microservices; API gateway; multi-tenant company/product scoping  
- **MovaCore hook:** Shared FastAPI + Postgres/Redis serving Parts storefront, Service/find-service, Marketing cabinets, and Flutter App. **[owner]** how companies/products are isolated in practice.

## 2. Python

**Q:** Where do you use synchronous vs asynchronous Python in the backend, and why?

- **Checks:** asyncio literacy; blocking I/O awareness  
- **Knowledge:** FastAPI/uvicorn, thread pools, supplier HTTP clients, RQ workers  
- **MovaCore hook:** Request path vs Redis/RQ workers for slower jobs. **[owner]** concrete examples of what must not block the event loop.

## 3. FastAPI

**Q:** How do you organize routes, dependencies, and auth across store vs platform cabinets?

- **Checks:** DI, middleware, role boundaries  
- **Knowledge:** APIRouter, Depends, session/cookie vs token patterns  
- **MovaCore hook:** `/cabinet/` platform admin vs `/s/{slug}/store/` store cabinet vs public storefront. **[owner]** how authz is enforced for find-service admin metrics.

## 4. PostgreSQL

**Q:** What data lives in Postgres vs Redis, and how do you reason about consistency?

- **Checks:** durable vs ephemeral state  
- **Knowledge:** transactions, indexes, migrations, JSON columns if used  
- **MovaCore hook:** Orders/leads/bookings durability vs shop search cache. **[owner]** migration habits and any painful schema changes.

## 5. Redis

**Q:** How does Redis support Parts search correctness (especially OEM → analogs)?

- **Checks:** cache invalidation / poison-cache awareness  
- **Knowledge:** TTLs, key design, cache-aside  
- **MovaCore hook:** Guards against caching “primary without analogs” frames; analog merge from CrossesList. **[owner]** a bug that taught the guard.

## 6. REST API

**Q:** How do mobile and web clients share the same domain APIs without duplicated business rules?

- **Checks:** API-first design, versioning, error contracts  
- **Knowledge:** OpenAPI, status codes, idempotency for orders/bookings  
- **MovaCore hook:** Flutter App + React cabinets against shared FastAPI. Portfolio mirror: `examples/api/demo_app.py`. **[owner]** versioning strategy.

## 7. Flutter

**Q:** How is the companion app structured relative to Parts and Service backends?

- **Checks:** client architecture, offline/partial online thinking  
- **Knowledge:** Dart/Flutter navigation, state, secure storage for tokens  
- **MovaCore hook:** Garage, VIN path, parts, service booking screens. **[owner]** which features are production-stable vs evolving (calendar/reminders).

## 8. Supplier integrations

**Q:** Why API-first supplier sourcing instead of spreadsheet price uploads as the primary path?

- **Checks:** integration reliability, latency, ranking/merge  
- **Knowledge:** external API failures, timeouts, multi-source merge, rate limits  
- **MovaCore hook:** Rossko/Berg-style aggregation; OEM brand disambiguation; offer windows from store hours. **[owner]** worst supplier failure mode handled.

## 9. AI agents

**Q:** Where does Applied AI sit in MovaCore today — and what is deliberately *not* shipped?

- **Checks:** honesty about scope; production vs demo  
- **Knowledge:** agent loops, context snapshots, evaluation limits  
- **MovaCore hook:** Marketing ads agent is the confirmed production pattern; in-app automotive assistant is concept / teaching demo (`examples/ai/automotive_assistant.py`). **[owner]** why ads ops was the first AI surface.

## 10. Tool calling

**Q:** How do you prevent an LLM from calling arbitrary tools?

- **Checks:** allowlists, schema of tools, least privilege  
- **Knowledge:** function/tool calling APIs; policy gates  
- **MovaCore hook:** Ads action allowlist; demo `ALLOWED_TOOLS` / `SIDE_EFFECT_TOOLS` in automotive assistant. **[owner]** how allowlist changes are reviewed.

## 11. Structured outputs

**Q:** Why require JSON plans instead of free-form natural language for side effects?

- **Checks:** validation mindset; schema-first AI  
- **Knowledge:** JSON schema / Pydantic; response_format; repair vs reject  
- **MovaCore hook:** Structured agent plans → validate → store. Portfolio: `AgentPlan` / `AssistantAdvice`. **[owner]** what happens on invalid JSON in production.

## 12. Human-in-the-loop

**Q:** Which AI actions can run automatically, and which require a human apply step?

- **Checks:** safety for money-moving / booking actions  
- **Knowledge:** dry-run, approve/reject, audit logs  
- **MovaCore hook:** Ads plan apply; demo booking/order tools queued until `approved_by_human`. **[owner]** UX of the review screen.

## 13. Security

**Q:** How do you keep supplier keys, ads OAuth, and customer PII out of clients and public repos?

- **Checks:** secret hygiene; threat model basics  
- **Knowledge:** env on server, least privilege, public portfolio boundary  
- **MovaCore hook:** This portfolio never contains `.env` or private source; cabinets stay authenticated. **[owner]** incident or near-miss around secrets.

## 14. Error handling

**Q:** Walk through failure modes when a supplier times out mid-search or an LLM call fails.

- **Checks:** partial results, user messaging, retries  
- **Knowledge:** timeouts, circuit ideas, graceful degradation  
- **MovaCore hook:** Search UX that still shows progressive results; LLM retries in demo `HttpLLMClient`. **[owner]** production observability today (partial).

## 15. Scaling

**Q:** If Parts search traffic 10× next month, what would you change first — and what would you *not* rewrite yet?

- **Checks:** pragmatic scaling; bottlenecks  
- **Knowledge:** caching, worker capacity, DB indexes, horizontal API replicas  
- **MovaCore hook:** Redis cache + RQ workers + Docker Compose on a VPS today. **[owner]** measured bottlenecks vs hypothesized ones (no invented metrics).

---

## How to use this doc

1. For each question, write 3–5 bullet talking points privately (do not commit secrets).  
2. Prefer one concrete incident over abstract buzzwords.  
3. Point interviewers at public artifacts: [architecture](architecture.md), [case studies](case-studies.md), [AI demo](ai-demo.md), `examples/`.  
