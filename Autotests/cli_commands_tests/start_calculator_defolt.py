import subprocess

def test_start_default():
    assert subprocess.run(["C:\\webcalculator.exe", "start"]).returncode == 0

test_start_default()