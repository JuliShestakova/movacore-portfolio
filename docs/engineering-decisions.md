# Engineering Decisions

Documented as observed in the private MovaCore system and reflected in this portfolio. Decisions are described at a level useful for review; proprietary implementation details stay private.

## 1. Multi-product hub on one backend

**Decision:** Run Parts, Service, Marketing, and App backends as product surfaces on a shared FastAPI platform rather than fully separate services from day one.

**Why:** Shared auth, persistence, and operational tooling reduce duplication while products remain conceptually bounded (cabinets and navigation stay product-scoped).

**Trade-off:** Stronger need for clear module boundaries; risk of a growing monolith if domains are not disciplined.

## 2. API-first parts availability

**Decision:** Prefer supplier APIs (e.g. Rossko, Berg) as the primary availability source instead of Excel/CSV price lists as the main path.

**Why:** Fresher offers, fewer manual sync errors, clearer ownership of “sources of availability” in the store cabinet.

**Trade-off:** Dependency on supplier uptime, rate limits, and response-shape variance; requires server-side aggregation and caching discipline.

## 3. Redis cache with correctness guards

**Decision:** Cache shop search aggressively, but drop or refuse frames that would mark OEM results as fully resolved without required analog/cross data.

**Why:** A fast but wrong “primary only” cache is worse than a slower correct merge for OEM → analog UX.

## 4. Cabinets driven by navigation config

**Decision:** Structure store/service operator UIs around explicit navigation trees (JSON-driven menus) rather than ad-hoc admin pages.

**Why:** Forces product completeness (pricing, delivery, reviews, analytics remain first-class) and keeps IA consistent as modules land.

## 5. Applied AI with allowlists and human apply

**Decision:** For ads-ops AI, use structured JSON plans, allowlisted tools, policy gates, dry-run, and human confirmation before side effects.

**Why:** Advertising mutations are high-risk; unconstrained agent autonomy is unacceptable for production spend.

## 6. Flutter companion on the same domain model

**Decision:** Build MovaCore App in Flutter against the same platform APIs as web Parts/Service.

**Why:** One ecosystem story for vehicle owners (garage, parts, bookings) without maintaining a separate business backend for mobile.

## 7. Portfolio repo separated from private production

**Decision:** Publish architecture, rewritten demos, and documentation — never the private tree, secrets, or commit history.

**Why:** Enables OpenAI / hiring review without exposing tenant data, commercial logic, or infrastructure internals.
