import asyncio
from datetime import datetime

import pytest
from packaging.version import Version

from pipt.core.index import get_vmax_for_package
from pipt.core.options import Options


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def make_meta(releases):
    # Build a minimal PyPI JSON-like dict
    # releases: dict version -> list of files with upload_time_iso_8601 and requires_python/yanked
    return {"releases": releases}


def iso(ts: str):
    return ts


def dt(ts: str):
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts)


@pytest.mark.parametrize("allow_pre", [False, True])
def test_vmax_basic_pre_release_handling(allow_pre):
    meta = make_meta(
        {
            "1.0.0rc1": [{"upload_time_iso_8601": "2020-01-01T00:00:00Z"}],
            "1.0.0": [{"upload_time_iso_8601": "2020-01-02T00:00:00Z"}],
            "1.1.0": [{"upload_time_iso_8601": "2020-02-01T00:00:00Z"}],
        }
    )
    cutoff = dt("2020-01-15T00:00:00Z")
    opts = Options(allow_pre=allow_pre)
    vmax = run(get_vmax_for_package(meta, cutoff, opts))
    if allow_pre:
        assert vmax == Version("1.0.0")
    else:
        assert vmax == Version("1.0.0")


def test_vmax_yanked_filtered():
    meta = make_meta(
        {
            "1.0.0": [
                {"upload_time_iso_8601": "2020-01-01T00:00:00Z", "yanked": True},
                {"upload_time_iso_8601": "2020-01-01T01:00:00Z", "yanked": True},
            ],
            "1.1.0": [{"upload_time_iso_8601": "2020-02-01T00:00:00Z"}],
        }
    )
    cutoff = dt("2020-01-15T00:00:00Z")
    opts = Options(allow_pre=False, allow_yanked=False)
    vmax = run(get_vmax_for_package(meta, cutoff, opts))
    assert vmax is None


def test_vmax_requires_python():
    meta = make_meta(
        {
            "1.0.0": [
                {"upload_time_iso_8601": "2020-01-01T00:00:00Z", "requires_python": ">=3.10"}
            ],
            "1.1.0": [
                {"upload_time_iso_8601": "2020-01-02T00:00:00Z", "requires_python": ">=3.6"}
            ],
        }
    )
    cutoff = dt("2020-01-03T00:00:00Z")
    vmax = run(get_vmax_for_package(meta, cutoff, Options(python_version="3.7")))
    assert vmax == Version("1.1.0")
    vmax2 = run(get_vmax_for_package(meta, cutoff, Options(python_version="3.9")))
    assert vmax2 == Version("1.1.0")


def test_vmax_cutoff():
    meta = make_meta(
        {
            "1.0.0": [{"upload_time_iso_8601": "2020-01-01T00:00:00Z"}],
            "1.1.0": [{"upload_time_iso_8601": "2020-02-01T00:00:00Z"}],
        }
    )
    cutoff = dt("2020-01-15T00:00:00Z")
    vmax = run(get_vmax_for_package(meta, cutoff, Options()))
    assert vmax == Version("1.0.0")
