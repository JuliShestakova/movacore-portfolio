# Stage 3 — Product UI Audit

Read-only assessment for the public portfolio. Status labels:

- **Works** — used in production / local development with real flows  
- **Partial** — UI/API exist; incomplete edge cases or polish  
- **In development** — actively being built  
- **Concept** — roadmap / idea only  

No invented metrics.

---

## MovaCore Parts

| Area | Status | Notes |
|---|---|---|
| Parts catalog / storefront | **Works** | Hypermarket-style public storefront |
| Search by article | **Works** | Server-side supplier aggregation |
| Search by VIN | **Works** | VIN-oriented discovery path exists |
| Search by name / text | **Partial** | Depends on supplier/catalog coverage |
| Search results + analogs | **Works** | OEM→cross merge with cache guards |
| Supplier offers | **Works** | API-first (e.g. Rossko, Berg) |
| Delivery / pickup labels | **Works** | Store hours windowing |
| Cart / checkout / orders | **Works** | Storefront + store cabinet |
| Store operator cabinet | **Works** | Requests, orders, suppliers, pricing, profile… |
| Pricing rules | **Partial / evolving** | Cabinet modules present |

Public storefront (Unicode domain connected for Parts): documented in `live-demo.md` without infrastructure internals.

---

## MovaCore Service

| Area | Status | Notes |
|---|---|---|
| Service discovery (list/map) | **Works** | Public find-service flows |
| Service card / profile | **Works** | Workshop profile + offers |
| Services / work catalog | **Works** | Offer selection for booking |
| Booking | **Works** | Public book + my bookings |
| Service operator cabinet | **Works** | Clients, posts, bookings |
| Appointment management | **Partial** | Via bookings / posts; calendar depth evolving |
| Platform admin for Service | **Works** | Live metrics in `/cabinet/admin/find-service` |

---

## MovaCore App (Flutter)

| Area | Status | Notes |
|---|---|---|
| Home / hub | **Works** | Hub home screen |
| Garage | **Works** | Add/manage vehicles |
| Add vehicle | **Works** | Garage flows |
| VIN catalog / scanner path | **Works** | VIN catalog screen |
| Parts catalog | **Works** | Parts + cart/checkout/orders |
| Find auto service | **Works** | Map/list/shop |
| Service booking | **Works** | Book + my bookings |
| Maintenance history | **Partial** | Service notes; full history productization evolving |
| Reminders | **Partial** | Reminder-kind notifications; dedicated UX evolving |
| Appointments calendar | **Partial** | Bookings list; richer calendar evolving |
| Push (FCM/APNs) | **Not confirmed as production** | Do not claim |
| In-app AI assistant | **Concept** | Documented as future; ads AI is on Marketing path |

---

## MovaCore Marketing

| Area | Status | Notes |
|---|---|---|
| Company marketing cabinet | **Works** | Posts, channels, queue, content tools |
| Leads / requests | **Works** | Manager inbox / CRM-adjacent flows |
| Analytics | **Partial** | Content/analytics views; depth varies |
| Calendar / media / monitoring | **Works / evolving** | Present in nav |
| Applied AI ads agent | **Works** (gated) | Structured plan → allowlist → human apply |
| Fully autonomous spend AI | **Concept / rejected design** | HITL preferred |
| Products hub | **Works** | `/cabinet/products` multi-product entry |

---

## Cross-cutting

| Area | Status |
|---|---|
| Shared FastAPI platform | **Works** |
| Postgres + Redis + RQ | **Works** |
| Docker Compose on VPS | **Works** |
| Platform owner admin | **Works** |
| Public portfolio demos (`examples/`) | **Works** (teaching code) |
