import pytest
from src.app.models.validation import (custom_validate_performance,
    get_expected_metrics,
    ValidationError)


@pytest.fixture
def metrics_values():
    return {
        "accuracy": 0
    }


def test_expected_metrics_exists():
    assert len(get_expected_metrics()) > 0


def test_raise_validation_error(metrics_values):
    with pytest.raises(ValidationError):
        custom_validate_performance(metrics_values)
