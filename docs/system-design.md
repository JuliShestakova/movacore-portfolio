# System Design

## Goals

1. Support multiple automotive products on one platform without collapsing concerns.
2. Keep operator cabinets (store / service / platform) distinct from consumer surfaces.
3. Prefer supplier APIs for availability over manual catalog uploads as the primary model.
4. Allow Applied AI where workflows can be structured, gated, and reviewed by a human.
5. Deploy and operate on commodity VPS infrastructure with Docker Compose.

## Non-Goals (for the public portfolio)

- Publishing private production code or commit history
- Benchmarks or revenue metrics that are not independently verified here
- Claiming unfinished product ideas as shipped features

## Bounded Contexts (conceptual)

| Context | Responsibilities |
|---|---|
| Identity & access | Users, sessions, roles for cabinets |
| Parts commerce | Search, offers, carts/orders/leads, store profile |
| Service ops | Discovery, booking, posts, clients, notes |
| Marketing ops | Ads-related tooling and AI advisor/agent |
| Platform admin | Multi-tenant overview, subscriptions, infra health views |

## Consistency & Caching

- PostgreSQL is the source of truth for durable business state.
- Redis accelerates read-heavy shop search and coordinates background jobs.
- Cache entries that would present incomplete OEM→analog results are treated as unsafe and must not be served as “fully resolved.”

## Multi-Tenancy Shape

Retailers and services operate through slug-scoped cabinet URLs and product entitlements. The platform owner cabinet is a separate surface for cross-tenant administration — not the same as a store cabinet.

## Mobile ↔ Platform Continuity

The Flutter app consumes the same product domains (garage vehicles, parts search, service booking). Synchronization is API-driven; offline-first sync is not claimed as a complete production capability unless later documented with evidence.

## Evolution Strategy

Ship vertical slices (cabinet module, supplier connector, booking flow) behind clear navigation configs and API contracts. AI features follow the same rule: ship gated workflows, then expand tool coverage.
