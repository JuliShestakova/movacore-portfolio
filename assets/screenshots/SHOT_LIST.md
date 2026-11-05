# Screenshot Shot List (owner to capture)

Do **not** invent or AI-generate fake UI screenshots.  
Capture only from **test / staging** accounts with synthetic data.

## Rules

- No real customer names, phones, emails, addresses  
- No supplier API keys, account numbers, or internal hostnames/IPs  
- Blur or use demo articles (e.g. public OEM samples) when unsure  
- Prefer light mode frames consistent with current product UI  

## MovaCore Parts

| ID | Shot | Suggested filename | Notes |
|---|---|---|---|
| P1 | Storefront search results | `parts-search-results.png` | Demo article; show OEM + at least one analog row |
| P2 | Offer delivery window | `parts-delivery-label.png` | Availability / pickup window label visible |
| P3 | Store cabinet home | `store-cabinet-home.png` | Empty or test shop; no real leads PII |
| P4 | Suppliers / sources | `store-cabinet-suppliers.png` | API sources list without secrets |
| P5 | Orders or requests list | `store-cabinet-orders.png` | Filters visible; synthetic rows only |

## MovaCore Service

| ID | Shot | Suggested filename | Notes |
|---|---|---|---|
| S1 | Service map or list | `service-discovery.png` | Public discovery UI |
| S2 | Service cabinet clients | `service-cabinet-clients.png` | Synthetic clients only |
| S3 | Booking / posts | `service-cabinet-booking.png` | Test workshop |
| S4 | Platform admin → Find Service | `platform-admin-find-service.png` | Live metrics tabs (workshops / clients / app) |

## MovaCore App (Flutter)

| ID | Shot | Suggested filename | Notes |
|---|---|---|---|
| A1 | Garage | `app-garage.png` | Fictional vehicle |
| A2 | VIN / catalog | `app-vin-catalog.png` | Test VIN or masked |
| A3 | Parts search | `app-parts.png` | Same demo article family if possible |
| A4 | Service booking | `app-booking.png` | Test slot |
| A5 | Service notes | `app-notes.png` | Synthetic note |

## Platform / Marketing (optional)

| ID | Shot | Suggested filename | Notes |
|---|---|---|---|
| M1 | Products hub | `hub-products.png` | Product cards |
| M2 | Platform overview | `platform-admin-overview.png` | No secrets in system panel |
| M3 | AI plan review UI | `marketing-ai-plan.png` | Dry-run / HITL screen if safe to show |

## After capture

1. Place files in `assets/screenshots/`  
2. Reference them from `README.md`  
3. Re-run security checklist (no PII in pixels)  
