from examples.python.errors import ApiError


def test_api_error_to_dict_strips_secrets() -> None:
    err = ApiError(
        code="upstream_failed",
        message="Supplier unavailable",
        status_code=502,
        details={"authorization": "Bearer secret", "retry_after": 3},
    )
    payload = err.to_dict()
    assert payload["error"]["code"] == "upstream_failed"
    assert "authorization" not in payload["error"]["details"]
    assert payload["error"]["details"]["retry_after"] == 3


def test_api_error_without_details() -> None:
    err = ApiError(code="bad_request", message="Invalid article", status_code=400)
    assert "details" not in err.to_dict()["error"]
