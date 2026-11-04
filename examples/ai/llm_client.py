"""Abstract LLM client with timeout/retry — demo only, no real keys required for tests."""

from __future__ import annotations

import abc
import asyncio
import logging
import os
from typing import Any, Optional

logger = logging.getLogger("movacore.demo.ai")


class LLMError(RuntimeError):
    pass


class LLMClient(abc.ABC):
    @abc.abstractmethod
    async def complete_json(self, system: str, user: str) -> dict[str, Any]:
        raise NotImplementedError


class EchoLLMClient(LLMClient):
    """Deterministic stand-in for unit tests and offline demos."""

    def __init__(self, payload: Optional[dict[str, Any]] = None) -> None:
        self.payload = payload or {
            "actions": [{"type": "add_negative_keyword", "value": "free"}],
            "rationale": "demo",
        }

    async def complete_json(self, system: str, user: str) -> dict[str, Any]:
        logger.info("echo_llm system_len=%s user_len=%s", len(system), len(user))
        return dict(self.payload)


class HttpLLMClient(LLMClient):
    """Skeleton for an OpenAI-compatible gateway. Not used in CI by default."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
        timeout: float = 20.0,
        retries: int = 2,
    ) -> None:
        self.api_key = api_key or os.getenv("LLM_API_KEY", "")
        self.base_url = (base_url or os.getenv("LLM_BASE_URL", "")).rstrip("/")
        self.model = model or os.getenv("LLM_MODEL", "demo-model")
        self.timeout = timeout
        self.retries = retries

    async def complete_json(self, system: str, user: str) -> dict[str, Any]:
        if not self.api_key or self.api_key.startswith("sk-demo"):
            raise LLMError("LLM_API_KEY is not configured for live calls")

        # Import lazily so demo tests do not require network usage.
        import httpx

        last_exc: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    # Placeholder shape — adapt to your gateway in private code.
                    resp = await client.post(
                        f"{self.base_url}/chat/completions",
                        headers={"Authorization": f"Bearer {self.api_key}"},
                        json={
                            "model": self.model,
                            "messages": [
                                {"role": "system", "content": system},
                                {"role": "user", "content": user},
                            ],
                            "response_format": {"type": "json_object"},
                        },
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    content = data["choices"][0]["message"]["content"]
                    import json

                    return json.loads(content)
            except Exception as exc:  # noqa: BLE001 — demo retry envelope
                last_exc = exc
                logger.warning("llm_attempt_failed attempt=%s err=%s", attempt, type(exc).__name__)
                await asyncio.sleep(0.2 * (attempt + 1))
        raise LLMError(f"LLM call failed: {type(last_exc).__name__}")
