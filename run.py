  GNU nano 2.7.4                                                              File: main.py                                                               Modified  

import subprocess

command = input("Command: ").split()

def compute(cmd: list):
        base = ""
        for value in cmd:
                if "subprocess.call([" not in base:
                        base += "subprocess.call(["
                base += f"'{value}',"
        return base[:-1] + "])"

try:
        exec(compute(command))
        input()
except FileNotFoundError:
    print("Invalid Command")
    input()
