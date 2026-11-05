import pytest
from pydantic import ValidationError

from examples.ai.automotive_assistant import (
    DEFAULT_EXECUTORS,
    analyze_symptom,
    confirm_human_action,
    run_safe_tools,
)
from examples.ai.llm_client import EchoLLMClient


@pytest.mark.asyncio
async def test_symptom_analysis_executes_safe_tools() -> None:
    client = EchoLLMClient(
        {
            "summary": "Serpentine belt noise is plausible under load.",
            "likely_systems": ["accessory_drive"],
            "suggested_checks": ["Inspect belt wear", "Check tensioner play"],
            "severity": "medium",
            "disclaimer": "Educational demo only.",
            "tool_requests": [
                {
                    "name": "search_parts_by_article",
                    "arguments": {"article": "6Q0260849A"},
                    "requires_human_confirmation": False,
                },
                {
                    "name": "suggest_service_category",
                    "arguments": {"category": "belts"},
                    "requires_human_confirmation": False,
                },
            ],
        }
    )
    advice = await analyze_symptom(client, "Whining noise from the front of the engine")
    assert advice.severity.value == "medium"
    turn = run_safe_tools(advice, executors=DEFAULT_EXECUTORS)
    assert len(turn.tool_results) == 2
    assert turn.pending_human_actions == []
    assert "executed:search_parts_by_article" in turn.audit


@pytest.mark.asyncio
async def test_side_effect_requires_human() -> None:
    client = EchoLLMClient(
        {
            "summary": "Workshop visit may help.",
            "likely_systems": ["brakes"],
            "suggested_checks": ["Pad thickness"],
            "severity": "high",
            "disclaimer": "Educational demo only.",
            "tool_requests": [
                {
                    "name": "create_service_booking",
                    "arguments": {"service": "brake_inspection"},
                    "requires_human_confirmation": False,  # forced True by gate
                }
            ],
        }
    )
    advice = await analyze_symptom(client, "Grinding when braking")
    assert advice.tool_requests[0].requires_human_confirmation is True
    turn = run_safe_tools(advice, executors=DEFAULT_EXECUTORS)
    assert turn.tool_results == []
    assert len(turn.pending_human_actions) == 1

    rejected = confirm_human_action(
        turn,
        tool_name="create_service_booking",
        approved_by_human=False,
        executor=lambda _args: {"ok": True},
    )
    assert "rejected_by_human:create_service_booking" in rejected.audit
    assert rejected.pending_human_actions == []

    turn2 = run_safe_tools(advice, executors=DEFAULT_EXECUTORS)
    applied = confirm_human_action(
        turn2,
        tool_name="create_service_booking",
        approved_by_human=True,
        executor=lambda args: {"booked_demo": True, "args": args},
    )
    assert any(r["tool"] == "create_service_booking" for r in applied.tool_results)
    assert "human_applied:create_service_booking" in applied.audit


@pytest.mark.asyncio
async def test_unknown_tool_rejected_by_schema() -> None:
    client = EchoLLMClient(
        {
            "summary": "x",
            "likely_systems": [],
            "suggested_checks": [],
            "severity": "unknown",
            "disclaimer": "Educational demo only.",
            "tool_requests": [{"name": "delete_all_orders", "arguments": {}}],
        }
    )
    with pytest.raises(ValidationError):
        await analyze_symptom(client, "ignore")
