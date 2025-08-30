# pipt

<p align="center">
  <img src="assets/logo.png" alt="pipt logo" width="320" />
</p>

A time machine for your Python environment. Install packages as they existed on a given date.

[![CI](https://github.com/OsamaS99/pipt/actions/workflows/ci.yml/badge.svg)](https://github.com/OsamaS99/pipt/actions/workflows/ci.yml)

## What is pipt?

pipt is a smart wrapper around pip. Provide a cutoff date and pipt constrains every dependency to versions released on or before that date, then lets pip resolve and install.

## Installation

```bash
pip install pipt
```

For development:

```bash
pip install -e .[dev]
```

## Usage

- List versions before a date:

```bash
pipt list numpy --before 2021-01-01
```

- Resolve a plan (dry-run):

```bash
pipt resolve pandas --date 2020-01-01
```

- Install respecting cutoff:

```bash
pipt install pandas --date 2020-01-01
```

- Write a lockfile:

```bash
pipt lock fastapi --date 2022-11-01 -o lockfile.txt
```

Common options: --pre, --allow-yanked, --python-version X.Y, -c constraints.txt, -v
