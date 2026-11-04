"""Structured API error helpers without leaking secrets."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ApiError(Exception):
    code: str
    message: str
    status_code: int = 400
    details: Optional[dict[str, Any]] = None

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "error": {
                "code": self.code,
                "message": self.message,
            }
        }
        if self.details:
            # Never attach raw upstream bodies that may contain credentials.
            payload["error"]["details"] = {
                k: v for k, v in self.details.items() if k not in {"authorization", "api_key", "token"}
            }
        return payload
