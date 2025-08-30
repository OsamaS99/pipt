# Contributing to pipt

Thanks for your interest in contributing!

## Dev setup

- Create a virtualenv and install dev dependencies:
  - pip install -e .[dev]
- Run tests:
  - pytest -q
- Lint:
  - ruff check . && ruff format --check .
- Type check:
  - mypy src

## VCR cassettes

Integration tests use pytest-vcr. On first run, real HTTP calls to PyPI are recorded into tests/cassettes. To re-record, set VCR_RECORD_MODE=all.

## Pull requests

- Include tests for changes.
- Update README and CHANGELOG.
- Keep commits focused and clear.
