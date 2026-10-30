from orders_pipeline.validators import normalize_country
import pytest


def test_normalize_country_lowercase():
    assert normalize_country("us") == "US"

def test_normalize_country_too_long():
    with pytest.raises(ValueError):
        normalize_country("USA")


