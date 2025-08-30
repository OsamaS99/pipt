import pytest

from pipt.core.options import Options


def test_options_valid_defaults():
    o = Options()
    assert o.binary_only is True
    assert o.max_iterations > 0


def test_options_invalid_python_version():
    with pytest.raises(ValueError):
        Options(python_version="3")
    with pytest.raises(ValueError):
        Options(python_version="three.nine")


def test_options_types():
    with pytest.raises(TypeError):
        Options(allow_pre="yes")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        Options(verbose="no")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        Options(binary_only="no")  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        Options(max_iterations=0)
    with pytest.raises(ValueError):
        Options(cache_ttl_seconds=-1)


def test_options_constraint_files_type():
    with pytest.raises(TypeError):
        Options(user_constraint_files="constraints.txt")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        Options(user_constraint_files=[1, 2])  # type: ignore[list-item]
