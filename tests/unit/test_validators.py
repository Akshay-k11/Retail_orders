from orders_pipeline.validators import normalize_country, is_valid_amount, normalize_status
import pytest

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("us", "US"),
        ("  in ", "IN"),
        ("De", "DE"),
        (None, None),
        ("", None),
        ("   ", None),
    ]
)
def test_normalize_country(raw, expected):
    assert normalize_country(raw) == expected 

@pytest.mark.parametrize(
    "raw",
    [
        "USA", "U", "123", "12 3", "12"
    ]
)
def test_normalize_country_invalid_raises(raw):
    with pytest.raises(ValueError):
        normalize_country(raw)

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("10.50", True),
        ("0", True),
        (7, True),
        ("-1", False),
        ("abc", False),
        ("", False),
        (None, False),
        (" 5 ", True),
        (0, True),
        ([1], False),
        ("inf", False)
    ],
    ids=["decimal_str", "zero_str", "int", "negative", "non_numeric", "empty", "none", "padded", "zero_int", "list", "inf_lower"]
)
def test_is_valid_amount(raw, expected):
    assert is_valid_amount(raw) == expected

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("placed", "PLACED"),
        (" shipped", "SHIPPED"),
        ("cancelled", "CANCELLED"),
        ("COMPLETED", "COMPLETED"),
    ],
    ids=["lower", "leading_space", "cancelled", "already_upper"],
)
def test_normalize_status_valid(raw, expected):
    assert normalize_status(raw) == expected

@pytest.mark.parametrize(
    "raw",
    ["done", "", " ", None, 123],
    ids=["unknown", "empty", "blank", "none", "int"],
)
def test_normalize_status_invalid_raises(raw):
    with pytest.raises(ValueError, match="Invalid status:"):
        normalize_status(raw)

