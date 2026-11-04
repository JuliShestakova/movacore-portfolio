"""Illustrative booking schemas (demo only)."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class BookingStatus(str, Enum):
    NEW = "new"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    DONE = "done"


class CreateBookingRequest(BaseModel):
    workshop_id: UUID
    vehicle_id: Optional[UUID] = None
    service_code: str = Field(..., min_length=1, max_length=64)
    start_at: datetime
    note: Optional[str] = Field(default=None, max_length=500)


class BookingResponse(BaseModel):
    id: UUID
    status: BookingStatus
    workshop_id: UUID
    service_code: str
    start_at: datetime
    created_at: datetime
