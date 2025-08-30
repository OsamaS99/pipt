# Changelog

## [0.1.7] - 2025-08-30

### Fixed
- Mypy typing errors in resolver (_suggest_python_from_specs) causing CI failures.

### Changed
- Publish workflow runs only on tag push (and manual dispatch) to avoid duplicate releases when also creating a GitHub Release.

## [0.1.6] - 2025-08-30

### Added
- Diagnose command to preflight environment and cutoff without installing.
- --date-mode flag with `before` (default) and `nearest` (experimental) strategies.
- --allow-source to opt out of binary-only behavior in historical mode.
- Minimum Python suggestion derived from wheel tags or Requires-Python in conflict messages.

### Changed
- Improved EnvironmentCompatibilityError with optional extra hints; removed package-specific hints to keep guidance generic.
- Smarter resolver messages now include “Latest allowed by cutoff” and “Requires-Python for <pkg>==<ver>”.
- Optional cutoff: without --date pipt behaves like pip, still offering improved diagnostics.

### Fixed
- Robust parsing of pip --report schema variants.
- Treat empty plans as “Nothing to do” instead of erroring.

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
