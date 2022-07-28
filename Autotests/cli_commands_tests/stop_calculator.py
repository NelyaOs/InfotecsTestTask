import subprocess

def test_close():
    assert subprocess.run(["C:\\webcalculator.exe", "stop"]).returncode == 0

test_close()