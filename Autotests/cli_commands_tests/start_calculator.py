import subprocess

def test_start():
    assert subprocess.run(["C:\\webcalculator.exe", "start", "localhost", "5413"]).returncode == 0

test_start()