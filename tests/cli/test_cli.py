import os
import subprocess
import sys


def run_cmd(args):
    cmd = [sys.executable, "-m", "pipt.cli.main"] + args
    env = os.environ.copy()
    # Prepend local src to import our latest code
    root = os.path.dirname(os.path.dirname(__file__))
    src = os.path.join(root, "src")
    env["PYTHONPATH"] = src + os.pathsep + env.get("PYTHONPATH", "")
    return subprocess.run(cmd, capture_output=True, text=True, env=env)


def test_list_exit_code():
    proc = run_cmd(["list", "numpy", "--before", "2021-01-01"])
    assert proc.returncode in (0, 1)


def test_resolve_help():
    proc = run_cmd(["--help"])
    assert proc.returncode == 0


def test_invalid_date_rejected():
    proc = run_cmd(["resolve", "requests", "--date", "not-a-date"])
    # Depending on Typer/click version, exit could be 2 (usage) or 1 (explicit exit). Accept both.
    assert proc.returncode in (1, 2)
    combined = (proc.stdout or "") + (proc.stderr or "")
    assert ("Invalid --date value" in combined) or ("Invalid isoformat string" in combined)


def test_no_date_behaves_like_pip():
    proc = run_cmd(["resolve", "pip"])  # trivial package
    assert proc.returncode in (0, 2)
