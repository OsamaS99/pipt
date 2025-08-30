import subprocess
import sys


def run_cmd(args):
    cmd = [sys.executable, "-m", "pipt.cli.main"] + args
    return subprocess.run(cmd, capture_output=True, text=True)


def test_list_exit_code():
    proc = run_cmd(["list", "numpy", "--before", "2021-01-01"])
    assert proc.returncode in (0, 1)


def test_resolve_help():
    proc = run_cmd(["--help"])
    assert proc.returncode == 0
