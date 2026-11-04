import pytest

from examples.ai.agent_workflow import apply_plan, propose_plan
from examples.ai.llm_client import EchoLLMClient


@pytest.mark.asyncio
async def test_propose_and_apply_with_hitl() -> None:
    client = EchoLLMClient(
        {
            "actions": [
                {"type": "add_negative_keyword", "value": "free"},
                {"type": "delete_campaign", "value": "nope"},  # not allowlisted
            ],
            "rationale": "reduce waste",
        }
    )
    stored = await propose_plan(client, context="demo snapshot")
    assert len(stored.plan.actions) == 1
    assert stored.plan.actions[0].type == "add_negative_keyword"

    applied: list[str] = []
    result = apply_plan(
        stored,
        approved_by_human=True,
        executor=lambda a: applied.append(str(a.type)),
    )
    assert result.status.value == "applied"
    assert applied == ["add_negative_keyword"]


@pytest.mark.asyncio
async def test_human_reject() -> None:
    stored = await propose_plan(EchoLLMClient(), context="x")
    result = apply_plan(stored, approved_by_human=False, executor=lambda a: None)
    assert result.status.value == "rejected"
