import datetime
import os
from core.command import Command


class HelpCommand(Command):
    name = "help"
    help = "Show Available Commands"

    def execute(self, args):
        if not args:
            print("Available Commands: ")
            for cmd in COMMANDS.values():
                print(f"- {cmd.name} : {cmd.help}")
            return
        
        cmd_name = args[0]
        cmd = COMMANDS.get(cmd_name)

        if not cmd:
            print(f"No help Availale for : {cmd_name}")
            return
        
        print(f"{cmd.name} -> {cmd.help}")


class ExitCommand(Command):
    name = "exit"
    help = "Exit the shell"

    def execute(self, args):
        raise SystemExit
    

class EchoCommand(Command):
    name = "echo"
    help = "Echo input Arguments"

    def execute(self, args):
        print(" ".join(args))

class DateCommand(Command):
    name = "date"
    help = "Show current date and time"

    def execute(self, args):
        print(datetime.datetime.now())

class ClearCommand(Command):
    name = "clear"
    help = "Clear the terminal"

    def execute(self, args):
        os.system("cls")

class WhoAmICommand(Command):
    name = "whoami"
    help = "show currently who logged in"

    def execute(self, args):
        print(os.getlogin())





COMMANDS = {
    cmd.name : cmd for cmd in [
        HelpCommand(),
        ExitCommand(),
        EchoCommand(),
        DateCommand(),
        ClearCommand(),
        WhoAmICommand()
    ]
}


def execute(cmd,args):
    if not cmd:
        return
    command = COMMANDS.get(cmd)
    if not command:
        print(f"Unknown Command: {cmd}")
        return
    command.execute(args)

    