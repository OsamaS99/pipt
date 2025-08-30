# Changelog

## [0.1.5] - 2025-08-30

### Fixed
- Publish workflow triggers broadened (release/workflow_dispatch) to ensure PyPI deployment runs when creating a GitHub Release.

## [0.1.4] - 2025-08-30

### Added
- Intelligent failure analysis for pip errors:
  - Detects environment compatibility issues (no matching wheel) and source build failures.
  - Provides actionable guidance (try older Python, move cutoff forward, or use -v for details).
- Verbose mode now prints the exact pip command and dumps raw stdout/stderr for dry-run and install.

### Changed
- More informative error panels in CLI with concise hints.

### Fixed
- Minor robustness improvements in resolver error handling.

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
