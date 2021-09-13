import subprocess

base = ""

command = input("Command: ").split()

def compute(cmd: list, execute: bool):
        if type(execute) is not bool:
                raise TypeError(f"Expected boolean in second arguement instead of {type(execute)}")
        elif type(cmd) is not list:
                raise TypeError(f"Expected list in first arguement instead of {type(cmd)}")
        global base
        for value in cmd:
                if "subprocess.call([" not in base:
                        base += "subprocess.call(["
                base += f"'{value}',"
        if execute:
                return exec(base[:-1] + "])")
        else:
                return base[:-1] + "])"

try:
        compute(cmd=command, execute=True)
        input()
except FileNotFoundError:
    print("Invalid Command")
    input()
