import pytest
from datetime import timezone

from pipt.core.timeutil import parse_cutoff


def test_parse_simple_date_end_of_day():
    dt = parse_cutoff("2021-01-01")
    assert dt.tzinfo is not None
    assert dt.hour == 23 and dt.minute == 59


def test_parse_iso_with_tz():
    dt = parse_cutoff("2021-01-01T12:34:56+00:00")
    assert dt.tzinfo is not None
    assert dt.hour == 12 and dt.minute == 34


def test_parse_zulu():
    dt = parse_cutoff("2021-01-01T00:00:00Z")
    assert dt.tzinfo is not None
    assert dt.utcoffset() == timezone.utc.utcoffset(dt)


def test_bad_date_raises():
    with pytest.raises(ValueError):
        parse_cutoff("not-a-date")
