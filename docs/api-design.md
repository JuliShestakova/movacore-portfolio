# API Design

## Style

MovaCore exposes **HTTP JSON APIs** via FastAPI. Clients include React SPAs and the Flutter app.

## Conventions (portfolio description)

- Resource-oriented routes grouped by product domain (shop, service, cabinet, mobile)
- Pydantic models for request/response validation on the private backend; mirrored teaching examples here
- Auth via session cookies and/or bearer-style tokens depending on client (exact private schemes omitted)
- Consistent error payloads with machine-readable codes where practical

## Example Contract (demonstration)

```http
POST /demo/v1/parts/search
Content-Type: application/json

{
  "article": "6Q0260849A",
  "brand": "VAG",
  "include_analogs": true
}
```

```json
{
  "query": { "article": "6Q0260849A", "brand": "VAG" },
  "items": [
    {
      "brand": "GATES",
      "article": "6PK1735",
      "price": 1250.0,
      "currency": "RUB",
      "availability": "in_stock",
      "delivery_label": "today 10:00–19:00"
    }
  ],
  "meta": { "source": "demo", "cached": false }
}
```

Full demo models: `examples/api/` and `examples/schemas/`.

## External Integrations (server-side)

| Integration | Purpose | Client exposure |
|---|---|---|
| Supplier APIs | Parts offers / crosses | Never; aggregated server-side |
| LLM gateway | Structured AI plans | Never; keys stay on server |
| Ads APIs | Campaign operations | Never; agent tools mediate |

## Versioning

Private APIs evolve with the products. This portfolio versions **demo** endpoints under `/demo/v1` only.
