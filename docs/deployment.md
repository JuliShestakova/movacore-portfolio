# Deployment

## Production Pattern (described without internals)

1. Build or pull container images for the API and workers.  
2. Start the Compose stack on the VPS (Postgres, Redis, app, workers).  
3. Apply database migrations / schema updates as required by the private release process.  
4. Serve web assets (SPA) through the configured reverse proxy / app static pipeline.  
5. Verify health of API, Redis connectivity, and critical product routes.  

Exact hostnames, IPs, SSH procedures, and credentials are **excluded** from this repository.

## Environments

| Environment | Purpose | Public detail |
|---|---|---|
| Local development | Feature work on private repos | Not published |
| Staging / test | Safe screenshots & QA | Preferred for portfolio media |
| Production VPS | Live tenants | Architecture only |

## Mobile Distribution

Flutter APK/IPA builds are part of the private/mobile workflow. Public portfolio may reference that a companion app exists; build pipelines and signing keys stay private.

## Rollback Mentality

Prefer reversible config and database changes; keep AI tool policies conservative so a bad model output cannot freely mutate ad spend without human apply.
