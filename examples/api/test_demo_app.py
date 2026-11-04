from fastapi.testclient import TestClient

from examples.api.demo_app import app

client = TestClient(app)


def test_health() -> None:
    resp = client.get("/demo/v1/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_parts_search_includes_analog() -> None:
    resp = client.post(
        "/demo/v1/parts/search",
        json={"article": "6Q0260849A", "brand": "VAG", "include_analogs": True},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["items"][0]["article"] == "6Q0260849A"
    assert any(i["is_analog"] for i in data["items"])
