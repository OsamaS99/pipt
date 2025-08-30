import pytest

from pipt.core.timeutil import parse_cutoff


def test_parse_simple_date_end_of_day_utc():
    dt = parse_cutoff("2021-01-01")
    assert dt.tzinfo is not None
    assert dt.hour == 23 and dt.minute == 59 and dt.second == 59 and dt.microsecond == 999999


def test_parse_iso_with_z():
    dt = parse_cutoff("2021-01-01T12:30:00Z")
    assert dt.tzinfo is not None
    assert dt.hour == 12 and dt.minute == 30


def test_parse_iso_with_offset():
    dt = parse_cutoff("2021-01-01T12:30:00+02:00")
    assert dt.tzinfo is not None


def test_parse_invalid_then_raises():
    with pytest.raises(ValueError):
        parse_cutoff("not-a-date")
