# Full Product Screen Audit — MovaCore

Read-only inventory for the public portfolio (Stage 3 expansion).  
Status labels: **Works** · **Partial** · **Auth-required** · **Unavailable** · **Concept**

No private source was modified. No commit/push in this pass.

---

## Products found

| Product | Surface | Primary access |
|---|---|---|
| MovaCore Parts | Public storefront | `https://гипермаркет-автозапчастей.рф/` (mirror: `https://movacore.ru/s/hypermarket/`) |
| MovaCore Parts | Store operator cabinet | `/s/{slug}/store/` — auth |
| MovaCore Service | Customer discovery | Primarily **Flutter app** (no separate anonymous public web storefront confirmed) |
| MovaCore Service | Service operator cabinet | `/service/{slug}/cabinet/` — auth |
| MovaCore Marketing | Public marketing site | `https://movacore.ru/` |
| MovaCore Marketing | Company cabinet (social/content/CRM) | `/cabinet/` SPA after login — auth |
| Platform admin | Owner admin | `/cabinet/admin/*` — auth |
| Products hub | Multi-product entry | `/products` — auth |
| MovaCore App | Flutter companion | Emulator/device — local API or `movacore.ru` |

---

## 1. MovaCore Parts — public storefront

| Screen | Status | Demo priority | Screenshot |
|---|---|---|---|
| Home / hero + search | Works | High | [`parts/parts-home.png`](../assets/screenshots/parts/parts-home.png) |
| Search with article filled | Works | High | [`parts/parts-search.png`](../assets/screenshots/parts/parts-search.png) |
| Brand disambiguation results | Works | High | [`parts/parts-results.png`](../assets/screenshots/parts/parts-results.png) |
| Offers / product header (OEM + analogs tabs) | Works | High | [`parts/parts-offer.png`](../assets/screenshots/parts/parts-offer.png) |
| Empty cart drawer | Works | Medium | [`parts/parts-cart.png`](../assets/screenshots/parts/parts-cart.png) |
| Lead / request modal | Works | Medium | [`parts/parts-lead.png`](../assets/screenshots/parts/parts-lead.png) |
| Customer login / register overlays | Works | Medium | Not captured this pass (modal exists) |
| Garage (guest empty / after login) | Partial | Medium | Auth for VIN catalog path |
| My orders / returns | Auth-required | Medium | — |
| Checkout with items | Works (needs cart item) | High | Needs demo cart fill without PII |
| Category / brand browsing blocks | Works | Low | — |
| Delivery / FAQ sections | Works | Low | Visible on home scroll |

**Demo article used:** `6Q0260849A` (public OEM sample).

---

## 2. MovaCore Parts — store cabinet

Route base: `/s/{slug}/store/` (login: `/s/{slug}/store/login`).

| Screen (nav) | Status | Demo priority | Screenshot |
|---|---|---|---|
| Login | Works (public) | High | [`admin/store-cabinet-login.png`](../assets/screenshots/admin/store-cabinet-login.png) |
| Overview `#home` | Auth-required | High | — |
| My store `#store` | Auth-required | High | — |
| Delivery `#delivery` | Auth-required | Medium | — |
| Reviews `#reviews` | Auth-required / evolving | Medium | — |
| Orders `#orders` | Auth-required | High | — |
| Leads / requests `#leads` | Auth-required | High | — |
| Returns `#returns` | Auth-required | Medium | — |
| Clients `#clients` | Auth-required | Medium | — |
| Suppliers `#sources` | Auth-required | High | — |
| Pricing `#pricing` | Auth-required / partial | High | — |
| CRM `#crm` | Partial (МойСклад; others later) | Medium | — |
| Sales analytics `#sales` | Auth-required / partial | Medium | — |
| Staff `#staff` | Auth-required | Low | — |
| Billing `#billing` | Auth-required | Low | — |
| Settings `#settings` | Auth-required | Medium | — |

---

## 3. MovaCore Service — customer surfaces

| Screen | Status | Demo priority | Screenshot |
|---|---|---|---|
| Dedicated public web discovery (list/map) | **Unavailable** as separate anonymous public URL in this audit | High if exists | — |
| Service listing / map / filters | Works in **Flutter** | High | Needs app capture |
| Service card / detail | Works in Flutter | High | — |
| Book appointment | Works in Flutter | High | — |
| My bookings | Auth-required (app) | Medium | — |
| Reviews / favorites / city picker | Works / partial in Flutter | Medium | — |

**Note:** Marketing site describes “Найти автосервис”, but customer UX for discovery is implemented in the Flutter companion + service APIs, not as a Parts-style public web catalog URL.

---

## 4. MovaCore Service — operator cabinet

Route base: `/service/{slug}/cabinet/` (login confirmed public).

| Screen | Status | Demo priority | Screenshot |
|---|---|---|---|
| Login | Works (public) | High | [`service/service-cabinet-login.png`](../assets/screenshots/service/service-cabinet-login.png) |
| Overview `home` | Auth-required | High | — |
| Profile `profile` | Auth-required | High | — |
| Services catalog flags `services` | Auth-required | High | — |
| Calls `calls` | Auth-required | High | — |
| Clients `clients` | Auth-required | High | — |
| Reviews `reviews` | Auth-required | Medium | — |
| Analytics `analytics` | Auth-required / partial | Medium | — |
| Posts `posts` | Auth-required | Medium | — |
| Staff `staff` | Auth-required | Low | — |
| Billing `billing` | Auth-required | Low | — |
| Settings `settings` | Auth-required | Medium | — |

Example public login hostname path (no secrets):  
`https://movacore.ru/service/yuliya-servis/cabinet/login`

---

## 5. MovaCore Marketing — public + company cabinet

### Public marketing site

| Screen | Status | Demo priority | Screenshot |
|---|---|---|---|
| Landing hero | Works | High | [`marketing/marketing-home.png`](../assets/screenshots/marketing/marketing-home.png) |
| Product directions / cards | Works | High | [`marketing/marketing-products.png`](../assets/screenshots/marketing/marketing-products.png) |
| Platform login modal | Works | High | [`admin/platform-login.png`](../assets/screenshots/admin/platform-login.png) |

Laptop UI on the landing is **marketing illustration**, not a live authenticated session.

### Company marketing cabinet (`App.tsx` under `/`)

| Route | Status | Demo priority | Screenshot |
|---|---|---|---|
| Dashboard `/` | Auth-required | High | — |
| Leads `/leads` | Auth-required | High | — |
| Queue `/queue` | Auth-required | High | — |
| Posts `/posts` | Auth-required | High | — |
| Channels `/channels` | Auth-required | Medium | — |
| Calendar `/calendar` | Auth-required | Medium | — |
| Analytics `/analytics` | Auth-required / partial | High | — |
| Media `/media` | Auth-required | Medium | — |
| Monitoring `/monitoring` | Auth-required | Medium | — |
| Curation `/curation` | Auth-required | Medium | — |
| CRM `/crm` | Auth-required | Medium | — |
| Suppliers `/suppliers` | Auth-required | Low (cross-product) | — |
| Parts `/parts` | Auth-required | Low | — |
| Secretary `/secretary` | Auth-required / evolving | Medium | — |
| Settings / Account | Auth-required | Low | — |
| Ads AI plan review | Auth-required (HITL) | High for Applied AI | — |

---

## 6. Platform admin

Base: `/cabinet/admin/*` (ProtectedRoute).

| Route | Status | Demo priority | Screenshot |
|---|---|---|---|
| Overview | Auth-required | High | — |
| Social | Auth-required | Medium | — |
| Hypermarket | Auth-required | High | — |
| Find Service | Auth-required | High | — |
| Users | Auth-required | Medium | — |
| Payments | Auth-required | Medium | — |
| Companies | Auth-required | High | — |
| System | Auth-required | Medium (no secrets in shot) | — |
| Ranking | Auth-required | Medium | — |
| Audit | Auth-required | Medium | — |
| Products hub `/products` | Auth-required | High | — |

Login entry captured as platform login modal (shared with marketing site).

---

## 7. MovaCore App (Flutter)

Shell tabs: Home · Parts · Services · Orders · Profile.

| Screen file | Purpose | Auth | Status | Screenshot |
|---|---|---|---|---|
| `hub_home_screen.dart` | Hub home | Guest OK | Works | [`mobile-app/app-home.png`](../assets/screenshots/mobile-app/app-home.png) |
| `parts_screen.dart` | Parts search | Guest OK | Works | [`mobile-app/app-parts.png`](../assets/screenshots/mobile-app/app-parts.png) |
| `home_screen.dart` | Service discovery hub | Guest OK | Works | — |
| `list_screen.dart` / `map_screen.dart` | Service list/map | Guest OK | Works | — |
| `service_detail_screen.dart` | Service card | Guest OK | Works | — |
| `book_screen.dart` | Booking | Often auth | Works | — |
| `garage_screen.dart` | Garage | Auth preferred | Works | [`mobile-app/app-garage.png`](../assets/screenshots/mobile-app/app-garage.png) |
| `vin_catalog_screen.dart` | VIN catalog | Auth | Works | — |
| `cart_screen.dart` / `checkout_screen.dart` | Cart / checkout | Partial auth | Works | — |
| `orders_screen.dart` | Orders | Auth | Works | — |
| `my_bookings_screen.dart` | Bookings calendar-ish | Auth | Partial | — |
| `service_notes_screen.dart` | Service history notes | Auth | Partial | — |
| `notifications_screen.dart` | Notices / reminders | Partial | Partial | — |
| `profile_screen.dart` / `login_screen.dart` | Profile / login | — | Works | — |
| `owner_cabinet_screen.dart` | Owner shortcut | Auth | Partial | — |
| Others (filters, favorites, city, reviews, calls, splash, settings) | Supporting | Mixed | Works / partial | — |

### Flutter capture attempt (this session)

| Attempt | Result |
|---|---|
| Android emulator (`emulator-5554`) | **Failed** — Gradle/Kotlin daemon OOM (`insufficient memory`) |
| Windows desktop | **Failed** — Windows desktop project not configured |
| Chrome web | **Failed** — web not configured; Chrome debug launch failed |

**Conclusion:** App screens remain **unavailable for portfolio PNGs until the owner captures from a working emulator/device** (or provides a prebuilt debug APK + test login).

---

## Captured screenshots summary (13)

```text
assets/screenshots/
  parts/        6 PNGs (home, search, results, offer, cart, lead)
  marketing/    2 PNGs (home, products) — products recaptured without URL tooltip
  admin/        2 PNGs (store cabinet login, platform login)
  service/      1 PNG  (service cabinet login)
  mobile-app/   2 PNGs (app-home, app-parts) — owner-provided device captures
```

Target 15–20 quality frames: **13 achieved**. Remaining high-value frames need owner test accounts + more Flutter captures (garage, services, booking).

**Note on `app-home.png`:** demo VW Touran, plate `А 123 АА 123`, city Краснодар (synthetic). City picker can show Москва/Краснодар for the same garage — one home frame is enough.

---

## Unavailable / blocked without owner

| Need | Why |
|---|---|
| Store cabinet interior (home, orders, suppliers, pricing) | Auth |
| Service cabinet interior (home, calls, clients, services) | Auth |
| Marketing cabinet (dashboard, posts, AI plan) | Auth |
| Platform admin (overview, find-service, companies) | Auth |
| Flutter app main scenarios | Build/runtime capture failed on agent machine |
| Anonymous public Service web discovery | Not found as a separate public storefront URL |

---

## Required from the owner

### Test accounts (synthetic data only)

1. **Store operator** — Parts store cabinet (`/s/hypermarket/store/`)  
2. **Service operator** — Service cabinet (`/service/{slug}/cabinet/`)  
3. **Marketing company user** — `/cabinet/` content/leads  
4. **Platform owner admin** — `/cabinet/admin/` (especially Find Service)  
5. Optional: **app customer** phone for Flutter garage/bookings  

### Capture help

6. Flutter screenshots from emulator/device (or fix local Android memory / provide APK):  
   hub home, garage, parts, service list, service card, book, bookings/calendar  
7. Confirm whether any **public** Service discovery web URL should be published  
8. Explicit OK before any git push of this expansion  

---

## Safety notes

- Login screens captured **empty** (no credentials typed).  
- Parts demos used public OEM article only.  
- No VPS IPs, SSH, `.env`, or customer PII published.  
- Marketing laptop dashboard names are **landing mockup art**.  
- Private repositories were not modified.
