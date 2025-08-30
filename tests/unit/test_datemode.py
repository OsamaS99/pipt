import pytest
from pipt.core.options import Options


def test_date_mode_validation():
    assert Options().date_mode == "before"
    assert Options(date_mode="nearest").date_mode == "nearest"
    with pytest.raises(ValueError):
        Options(date_mode="around")
