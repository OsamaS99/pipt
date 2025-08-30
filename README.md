<div align="center">
  <img src="assets/logo.png" alt="pipt Logo" width="400"/>
  <p align="center">
    The Python Package Time Machine
  </p>
  <p align="center">
    <strong>Install dependencies as they existed on any given date.</strong>
  </p>
  <p align="center">
    <a href="https://github.com/OsamaS99/pipt/actions"><img alt="CI" src="https://github.com/OsamaS99/pipt/actions/workflows/ci.yml/badge.svg"></a>
    <a href="https://pypi.org/project/pipt"><img alt="PyPI" src="https://img.shields.io/pypi/v/pipt"></a>
  </p>
</div>

---

`pipt` is a command-line tool that acts as a time machine for your Python environment. It allows you to install packages and their dependencies exactly as they were on a specific date, ensuring perfect historical reproducibility.

It's not a new package manager, but a smart wrapper around `pip`. It uses `pip`'s powerful resolver to do the heavy lifting, while it intelligently finds the right versions for you.

### Key Features

- **Reproducible Builds:** Guarantee that your project's dependencies are identical to what they were in the past.
- **Date-Based Resolution:** Specify a date, and `pipt` will find the latest package versions available on or before that day.
- **Lockfile Generation:** Create `pip`-compatible lockfiles for pinning dependencies to a specific point in time.
- **Smart Wrapper:** Leverages `pip`'s battle-tested engine, making it lightweight and reliable.
- **Polished UX:** A beautiful and intuitive command-line experience powered by `rich`.

### Installation

You can install `pipt` using `pip`:

```bash
pip install pipt
```

### How It Works

`pipt` works by iteratively refining version constraints. It starts with your requested packages, finds the latest versions that existed on the cutoff date, and then runs `pip`'s resolver in a dry-run. If any transitive dependencies are too new, `pipt` adds new constraints for them and repeats the process until a historically accurate dependency set is found.

### Usage

#### Install a Package

To install a package as it existed on a specific date, use the `install` command.

```bash
# Install pandas as it was on New Year's Day 2023
pipt install "pandas<2.0" 2023-01-01
```

`pipt` will resolve and install `pandas` and all its dependencies as they were on that date.

#### Resolve Dependencies (Dry-Run)

If you want to see what would be installed without actually installing anything, use the `resolve` command.

```bash
# See the dependency plan for flask on June 1st, 2022
pipt resolve flask 2022-06-01
```

This will output a table of packages and their resolved versions.

#### Create a Lockfile

To generate a `requirements.txt`-style lockfile, use the `lock` command.

```bash
# Lock Django and its dependencies to their state on March 15th, 2021
pipt lock django 2021-03-15 > requirements.lock

# You can then install from this lockfile with pip
pip install -r requirements.lock
```

You can also include file hashes for added security:

```bash
pipt lock django 2021-03-15 --include-hashes > requirements.lock
```

#### List Available Versions

To see all available versions of a package before a certain date, use `list`.

```bash
# List all versions of requests published before 2020
pipt list requests --before 2020-01-01
```

### Philosophy

`pipt` is designed to be **simple, complete, and lovable**.

- **Simple:** It does one thing well: date-based dependency resolution.
- **Complete:** It's a robust wrapper around `pip`, handling complex resolution scenarios and edge cases.
- **Lovable:** It provides a polished user experience that makes dependency management a little more enjoyable.

### Contributing

Contributions are welcome! Please see the [Contributing Guide](CONTRIBUTING.md) for more details.

### License

`pipt` is licensed under the [MIT License](LICENSE).
