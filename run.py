import subprocess

command = input("Command: ").split()
try:
    base = "subprocess.call(["
    for value in command:
        base += f"'{value}',"
    finalCmd = base[:-1] + "])"
    exec(finalCmd)
    input()
except Exception as e:
    print(e)
    input()
