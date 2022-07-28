import subprocess


def test_restart():
    assert subprocess.run(["C:\\webcalculator.exe", "restart"]).returncode == 0


test_restart()
