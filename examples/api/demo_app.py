"""Minimal FastAPI demo — patterns only, no private business logic."""

from __future__ import annotations

import logging
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from examples.schemas.parts import (
    Availability,
    OfferItem,
    PartsSearchRequest,
    PartsSearchResponse,
)

logger = logging.getLogger("movacore.demo.api")

app = FastAPI(
    title="MovaCore Portfolio Demo API",
    version="0.1.0",
    description="Safe demonstration endpoints for the public portfolio repository.",
)


@app.get("/demo/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/demo/v1/parts/search", response_model=PartsSearchResponse)
def search_parts(body: PartsSearchRequest) -> PartsSearchResponse:
    """Return deterministic demo offers — not live supplier data."""
    logger.info("parts_search article=%s brand=%s", body.article, body.brand)

    if body.article in {"", "INVALID"}:
        raise HTTPException(status_code=400, detail="Invalid article")

    items = [
        OfferItem(
            brand=body.brand or "OEM",
            article=body.article,
            price=1990.0,
            availability=Availability.IN_STOCK,
            delivery_label="today 10:00–19:00",
            is_analog=False,
        )
    ]
    if body.include_analogs:
        items.append(
            OfferItem(
                brand="GATES",
                article="6PK1735",
                price=1250.0,
                availability=Availability.TODAY,
                delivery_label="today 10:00–19:00",
                is_analog=True,
            )
        )

    return PartsSearchResponse(
        query=body,
        items=items,
        meta={"source": "demo", "cached": False},
    )


@app.exception_handler(Exception)
async def unhandled_error(_: Any, exc: Exception) -> JSONResponse:
    logger.exception("unhandled_error type=%s", type(exc).__name__)
    return JSONResponse(status_code=500, content={"detail": "Internal error"})
