import subprocess


def test_help():
    assert subprocess.run(["C:\\webcalculator.exe", "-h"]).returncode == 1
