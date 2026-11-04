"""Offer ranking helpers — teaching example inspired by storefront needs."""

from __future__ import annotations

from dataclasses import dataclass


AVAIL_RANK = {
    "in_stock": 0,
    "today": 1,
    "tomorrow": 2,
    "later": 3,
    "unknown": 4,
}


@dataclass(frozen=True)
class DemoOffer:
    brand: str
    article: str
    price: float
    availability: str
    supplier_rank: int = 100


def sort_offers(offers: list[DemoOffer]) -> list[DemoOffer]:
    """Sort by availability window, then price, then supplier rank."""

    return sorted(
        offers,
        key=lambda o: (
            AVAIL_RANK.get(o.availability, 99),
            o.price,
            o.supplier_rank,
            o.brand,
            o.article,
        ),
    )


def group_key(brand: str, article: str) -> str:
    """Brand must be part of the key so same PN across brands do not collapse."""

    return f"{brand.strip().upper()}::{article.strip().upper()}"
