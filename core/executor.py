import datetime
import os

def cmd_help(args):
    print("Available Commands:",", ".join(COMMANDS.keys()))

def cmd_exit(args):
    raise SystemExit

def cmd_echo(args):
    print(" ".join(args))

def cmd_date(args):
    print(datetime.datetime.now())

def cmd_clear(args):
    os.system("cls")


COMMANDS = {
    "help" : cmd_help,
    "exit" : cmd_exit,
    "echo" : cmd_echo,
    "date" : cmd_date,
    "clear" : cmd_clear
}

def execute(cmd,args):
    if not cmd:
        return
    command = COMMANDS.get(cmd)
    if not command:
        print(f"Unknown Command: {cmd}")
        return
    command(args)

    