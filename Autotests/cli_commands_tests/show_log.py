import subprocess

def test_show_log():
    assert subprocess.run(["C:\\webcalculator.exe", "show_log"]).returncode == 0


test_show_log()