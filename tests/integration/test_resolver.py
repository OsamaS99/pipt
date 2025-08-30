import asyncio
from datetime import datetime

import pytest
from packaging.requirements import Requirement

from pipt.core.options import Options
from pipt.core.resolver import resolve_dependency_plan


@pytest.mark.vcr()
@pytest.mark.xfail(reason="Resolver prototype; pip dry-run conflicts pending refinement")
def test_resolve_numpy_simple():
    cutoff = datetime.fromisoformat("2021-01-01T23:59:59+00:00")
    reqs = [Requirement("numpy")]
    opts = Options()
    result = asyncio.get_event_loop().run_until_complete(
        resolve_dependency_plan(reqs, cutoff, opts)
    )
    assert any(
        name == "numpy" and "<=1.20.0" in str(spec) for name, spec in result.constraints.items()
    )


@pytest.mark.vcr()
@pytest.mark.xfail(reason="Resolver prototype; transitive handling pending refinement")
def test_resolve_pandas_transitive():
    cutoff = datetime.fromisoformat("2020-01-01T23:59:59+00:00")
    reqs = [Requirement("pandas")]
    opts = Options()
    result = asyncio.get_event_loop().run_until_complete(
        resolve_dependency_plan(reqs, cutoff, opts)
    )
    assert "pandas" in result.constraints
    assert "numpy" in result.constraints


@pytest.mark.vcr()
@pytest.mark.xfail(reason="Resolver prototype; conflict messaging pending")
def test_resolve_conflict_version():
    cutoff = datetime.fromisoformat("2020-01-01T23:59:59+00:00")
    reqs = [Requirement("pandas==1.3.0")]
    opts = Options()
    with pytest.raises(Exception):
        asyncio.get_event_loop().run_until_complete(resolve_dependency_plan(reqs, cutoff, opts))


@pytest.mark.vcr()
@pytest.mark.xfail(reason="Resolver prototype; requires-python handling pending full fidelity")
def test_resolve_python_version_mismatch():
    cutoff = datetime.fromisoformat("2023-01-01T23:59:59+00:00")
    reqs = [Requirement("tensorflow")]
    opts = Options(python_version="3.7")
    with pytest.raises(Exception):
        asyncio.get_event_loop().run_until_complete(resolve_dependency_plan(reqs, cutoff, opts))
