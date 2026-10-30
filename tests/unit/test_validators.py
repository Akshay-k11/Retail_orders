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
        "USA", "U", "123", "12 3"
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
    ]
)
def test_is_valid_amount(raw, expected):
    assert is_valid_amount(raw) == expected


def test_normalize_status():
    with pytest.raises(ValueError, match= "Invalid status"):
        normalize_status("done")


