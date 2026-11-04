"""Illustrative parts-search schemas (demo only — not production models)."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Availability(str, Enum):
    IN_STOCK = "in_stock"
    TODAY = "today"
    TOMORROW = "tomorrow"
    LATER = "later"
    UNKNOWN = "unknown"


class PartsSearchRequest(BaseModel):
    article: str = Field(..., min_length=1, max_length=64)
    brand: Optional[str] = Field(default=None, max_length=64)
    include_analogs: bool = True

    @field_validator("article")
    @classmethod
    def normalize_article(cls, value: str) -> str:
        return value.strip().upper()


class OfferItem(BaseModel):
    brand: str
    article: str
    price: float = Field(..., ge=0)
    currency: str = "RUB"
    availability: Availability = Availability.UNKNOWN
    delivery_label: str = "requires confirmation"
    is_analog: bool = False


class PartsSearchResponse(BaseModel):
    query: PartsSearchRequest
    items: list[OfferItem]
    meta: dict[str, object] = Field(default_factory=dict)
