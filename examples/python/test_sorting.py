from examples.python.sorting import DemoOffer, group_key, sort_offers


def test_sort_prefers_in_stock_then_price() -> None:
    offers = [
        DemoOffer("B", "X", 100.0, "tomorrow"),
        DemoOffer("A", "Y", 90.0, "in_stock"),
        DemoOffer("C", "Z", 80.0, "in_stock"),
    ]
    ordered = sort_offers(offers)
    assert ordered[0].article == "Z"
    assert ordered[1].article == "Y"
    assert ordered[2].availability == "tomorrow"


def test_group_key_includes_brand() -> None:
    assert group_key("Gates", "6PK1735") != group_key("Lynx", "6PK1735")
