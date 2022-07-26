import subprocess

def close():
    subprocess.run(["C:\\webcalculator.exe", "stop"])

close()