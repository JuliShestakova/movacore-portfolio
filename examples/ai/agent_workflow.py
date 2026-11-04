"""Structured plan → allowlist → human apply (demo Applied AI workflow)."""

from __future__ import annotations

import logging
from enum import Enum
from typing import Any, Callable

from pydantic import BaseModel, Field, ValidationError

from examples.ai.llm_client import LLMClient

logger = logging.getLogger("movacore.demo.agent")

ALLOWED_ACTIONS = frozenset(
    {
        "change_bid",
        "add_negative_keyword",
        "pause_keyword",
        "enable_keyword",
    }
)


class PlanStatus(str, Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    REJECTED = "rejected"
    APPLIED = "applied"


class AgentAction(BaseModel):
    type: str
    value: str | float | int | dict[str, Any]


class AgentPlan(BaseModel):
    actions: list[AgentAction] = Field(default_factory=list)
    rationale: str = ""


class StoredPlan(BaseModel):
    status: PlanStatus = PlanStatus.DRAFT
    plan: AgentPlan
    audit: list[str] = Field(default_factory=list)


def gate_actions(plan: AgentPlan) -> AgentPlan:
    kept = [a for a in plan.actions if a.type in ALLOWED_ACTIONS]
    dropped = len(plan.actions) - len(kept)
    if dropped:
        logger.info("policy_dropped count=%s", dropped)
    return AgentPlan(actions=kept, rationale=plan.rationale)


async def propose_plan(client: LLMClient, context: str) -> StoredPlan:
    raw = await client.complete_json(
        system="Return JSON with keys actions[], rationale. Actions must be allowlisted types.",
        user=context,
    )
    try:
        plan = AgentPlan.model_validate(raw)
    except ValidationError as exc:
        logger.warning("invalid_llm_schema errors=%s", exc.error_count())
        raise
    gated = gate_actions(plan)
    return StoredPlan(plan=gated, audit=["proposed"])


def apply_plan(
    stored: StoredPlan,
    *,
    approved_by_human: bool,
    executor: Callable[[AgentAction], None],
) -> StoredPlan:
    if not approved_by_human:
        stored.status = PlanStatus.REJECTED
        stored.audit.append("rejected_by_human")
        return stored

    for action in stored.plan.actions:
        executor(action)
        stored.audit.append(f"applied:{action.type}")
    stored.status = PlanStatus.APPLIED
    return stored
