# About the Builder

## Profile

Entrepreneur and software product builder with a programming background.  
Currently deepening **Python engineering** skills while independently designing, shipping, and operating a real multi-product platform for the automotive industry.

This is **not** a claim of Senior Engineer, Lead Engineer, or AI Researcher titles.  
It is a record of hands-on product and systems work under real business constraints.

## Personal note

I started building MovaCore because I wanted to solve real problems I encountered while running an automotive business. What began as an effort to improve everyday business processes gradually evolved into a larger software ecosystem.

I enjoy working across the entire product lifecycle: understanding user problems, designing system architecture, implementing backend functionality, integrating APIs, and exploring how AI can make products more useful.

My goal is to grow into a strong Software Engineer specializing in Applied AI, building reliable AI-powered products that solve practical problems.

## Why MovaCore Exists

MovaCore grew from operating in the automotive domain in practice — parts, services, customer communication, and growth tooling — and from the gap between what fragmented SaaS tools offer and what a connected product ecosystem needs.

The builder’s role combines:

- product definition (Parts, Service, Marketing, companion App);
- architecture and backend implementation (FastAPI, data stores, caches, workers);
- web and mobile surfaces (React cabinets / storefronts, Flutter app);
- integrations (supplier APIs, ads APIs, LLM gateway);
- deployment and day-to-day operation on a VPS with Docker Compose;
- Applied AI workflows that stay gated and reviewable.

## Personal Contribution to MovaCore

| Area | Contribution (honest) |
|---|---|
| Product vision | Defined the multi-product ecosystem model: shared platform, product-scoped cabinets, owner vs tenant surfaces |
| Backend | Designed and evolved the FastAPI application, domain modules, auth/session flows, and product APIs |
| Parts commerce | Built storefront search orchestration, supplier API sourcing, OEM→analog merge rules, cache correctness guards |
| Service product | Service discovery/booking paths, service operator cabinet, shared SQLite/`panel.db` client/app-user stores |
| Marketing / AI | Structured LLM agent path for ads operations: snapshot → JSON plan → allowlist → human apply → audit |
| Frontend | React/Vite cabinets and storefront UX; navigation-driven module structure for store/service operators |
| Mobile | Flutter companion (garage, VIN/parts, services, bookings, notes) against the same platform APIs |
| Infrastructure | Docker Compose packaging, VPS operation, Redis/RQ workers, ongoing release and hotfix practice |
| Portfolio | Authored this public documentation repo with rewritten demos (no private source dump) |

## Engineering Focus

Priority themes in current work:

1. **Production Applied AI** — structured outputs, tool calling, policy gates, human-in-the-loop  
2. **Correctness under integration load** — supplier variance, cache safety, clear availability labels  
3. **Ecosystem continuity** — garage ↔ parts ↔ service ↔ bookings across web and mobile  
4. **Operability** — deployable Compose stack, observable failures, safe admin tooling  

## Learning Path (transparent)

- Strengthening typed Python, FastAPI patterns, testing, and AI evaluation discipline  
- Expanding observability (quality/cost/failure modes for LLM plans)  
- Keeping claims honest: unfinished ideas stay in roadmap, not in “shipped” tables  

## How to Read This Portfolio

- Architecture and case studies describe **real** private systems at a safe level of detail  
- `examples/` contains **rewritten** teaching code, not production source  
- Mobile and AI capability tables separate **implemented**, **partial**, and **planned**  

Related:

- [Engineering Case Studies](case-studies.md)  
- [Engineering Decisions](engineering-decisions.md)  
- [AI Integration](ai-integration.md)  
- [Mobile App](mobile-app.md)  
