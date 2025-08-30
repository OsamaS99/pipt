# Changelog

## [0.1.3] - 2025-08-30

This is the first public baseline release of pipt. It consolidates all prior work and sets up automated publishing.

### Features
- Time-aware dependency resolution with iterative constraints.
- CLI commands: `list`, `resolve`, `install`, `lock`.
- Caching for PyPI JSON metadata, polished output via `rich`, and Typer-based UX.

### CI/CD
- GitHub Actions CI across Python 3.9–3.12 (ruff, mypy, pytest).
- Trusted Publishing (OIDC) to PyPI via `publish.yml` workflow and `pypi` environment.

### Docs
- Improved README with Quickstart, usage examples, options, and compatibility notes.
- Wider logo and absolute image URL so it renders on PyPI.
- Badges for CI and PyPI.

### Tooling
- mypy configuration (`ignore_missing_imports`) and CLI typing fixes.
- `.gitignore` updated to exclude build/ and dist/.
- MIT `LICENSE` added.
