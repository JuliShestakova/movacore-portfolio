"""Safe teaching demo: AI Automotive Assistant with structured outputs + HITL.

Mirrors the production Applied AI pattern (allowlist → validate → human gate)
without copying private MovaCore source or calling live supplier/booking APIs.
"""

from __future__ import annotations

import logging
from enum import Enum
from typing import Any, Callable

from pydantic import BaseModel, Field, ValidationError, field_validator

from examples.ai.llm_client import LLMClient

logger = logging.getLogger("movacore.demo.automotive")

ALLOWED_TOOLS = frozenset(
    {
        "search_parts_by_article",
        "suggest_service_category",
        "lookup_maintenance_hint",
    }
)

# Side-effect tools are never auto-executed in this demo.
SIDE_EFFECT_TOOLS = frozenset(
    {
        "create_service_booking",
        "place_parts_order",
    }
)


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class ToolRequest(BaseModel):
    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    requires_human_confirmation: bool = False

    @field_validator("name")
    @classmethod
    def name_must_be_known(cls, value: str) -> str:
        if value not in ALLOWED_TOOLS and value not in SIDE_EFFECT_TOOLS:
            raise ValueError(f"unknown tool: {value}")
        return value


class AssistantAdvice(BaseModel):
    summary: str
    likely_systems: list[str] = Field(default_factory=list)
    suggested_checks: list[str] = Field(default_factory=list)
    severity: Severity = Severity.UNKNOWN
    disclaimer: str = (
        "Educational demo only — not a mechanical diagnosis. "
        "Confirm with a qualified technician before repairs."
    )
    tool_requests: list[ToolRequest] = Field(default_factory=list)


class AssistantTurn(BaseModel):
    advice: AssistantAdvice
    tool_results: list[dict[str, Any]] = Field(default_factory=list)
    pending_human_actions: list[ToolRequest] = Field(default_factory=list)
    audit: list[str] = Field(default_factory=list)


def gate_tool_requests(advice: AssistantAdvice) -> AssistantAdvice:
    """Keep allowlisted advice tools; force HITL flag on side-effect tools."""
    kept: list[ToolRequest] = []
    for req in advice.tool_requests:
        if req.name in SIDE_EFFECT_TOOLS:
            kept.append(
                ToolRequest(
                    name=req.name,
                    arguments=req.arguments,
                    requires_human_confirmation=True,
                )
            )
            continue
        if req.name in ALLOWED_TOOLS:
            kept.append(req)
        else:
            logger.info("policy_dropped_tool name=%s", req.name)
    return advice.model_copy(update={"tool_requests": kept})


async def analyze_symptom(client: LLMClient, user_message: str) -> AssistantAdvice:
    raw = await client.complete_json(
        system=(
            "Return JSON for an automotive assistant advice object with keys: "
            "summary, likely_systems[], suggested_checks[], severity, "
            "disclaimer, tool_requests[{name, arguments, requires_human_confirmation}]. "
            "Only request allowlisted tools. Mark booking/order tools as requiring confirmation."
        ),
        user=user_message,
    )
    try:
        advice = AssistantAdvice.model_validate(raw)
    except ValidationError as exc:
        logger.warning("invalid_assistant_schema errors=%s", exc.error_count())
        raise
    return gate_tool_requests(advice)


def run_safe_tools(
    advice: AssistantAdvice,
    *,
    executors: dict[str, Callable[[dict[str, Any]], dict[str, Any]]],
) -> AssistantTurn:
    """Execute only allowlisted non-side-effect tools. Queue HITL actions."""
    turn = AssistantTurn(advice=advice, audit=["analyzed"])
    for req in advice.tool_requests:
        if req.requires_human_confirmation or req.name in SIDE_EFFECT_TOOLS:
            turn.pending_human_actions.append(req)
            turn.audit.append(f"queued_for_human:{req.name}")
            continue
        executor = executors.get(req.name)
        if executor is None:
            turn.audit.append(f"missing_executor:{req.name}")
            continue
        result = executor(req.arguments)
        turn.tool_results.append({"tool": req.name, "result": result})
        turn.audit.append(f"executed:{req.name}")
    return turn


def confirm_human_action(
    turn: AssistantTurn,
    *,
    tool_name: str,
    approved_by_human: bool,
    executor: Callable[[dict[str, Any]], dict[str, Any]],
) -> AssistantTurn:
    pending = [r for r in turn.pending_human_actions if r.name == tool_name]
    if not pending:
        turn.audit.append(f"no_pending:{tool_name}")
        return turn
    req = pending[0]
    if not approved_by_human:
        turn.audit.append(f"rejected_by_human:{tool_name}")
        turn.pending_human_actions = [r for r in turn.pending_human_actions if r.name != tool_name]
        return turn
    result = executor(req.arguments)
    turn.tool_results.append({"tool": tool_name, "result": result})
    turn.pending_human_actions = [r for r in turn.pending_human_actions if r.name != tool_name]
    turn.audit.append(f"human_applied:{tool_name}")
    return turn


# Deterministic stub executors for offline demos / pytest.
def stub_search_parts(arguments: dict[str, Any]) -> dict[str, Any]:
    article = str(arguments.get("article", "")).strip() or "UNKNOWN"
    return {
        "article": article,
        "offers_demo": [{"brand": "DEMO", "price": 1000, "availability": "in_stock"}],
    }


def stub_suggest_service(arguments: dict[str, Any]) -> dict[str, Any]:
    category = str(arguments.get("category", "general")).strip() or "general"
    return {"category": category, "workshops_demo": [{"name": "Demo Auto Service", "city": "Demo City"}]}


def stub_maintenance_hint(arguments: dict[str, Any]) -> dict[str, Any]:
    topic = str(arguments.get("topic", "")).strip() or "general"
    return {"topic": topic, "hint": "Check fluid levels and listen for noise changes under load."}


DEFAULT_EXECUTORS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "search_parts_by_article": stub_search_parts,
    "suggest_service_category": stub_suggest_service,
    "lookup_maintenance_hint": stub_maintenance_hint,
}
