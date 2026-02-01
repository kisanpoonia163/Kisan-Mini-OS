import datetime
import os
from core.command import Command


class HelpCommand(Command):
    name = "help"
    help = "Show Available Commands"

    def execute(self, args,context):
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

    def execute(self, args,context):
        context.running = False
    

class EchoCommand(Command):
    name = "echo"
    help = "Echo input Arguments"

    def execute(self, args,context):
        print(" ".join(args))

class DateCommand(Command):
    name = "date"
    help = "Show current date and time"

    def execute(self, args,context):
        print(datetime.datetime.now())

class ClearCommand(Command):
    name = "clear"
    help = "Clear the terminal"

    def execute(self, args,context):
        os.system("cls")

class WhoAmICommand(Command):
    name = "whoami"
    help = "show System Identity"

    def execute(self, args,context):
        print(os.getlogin(),"v{context.version}")

class SetCommand(Command):
    name = "set"
    help = "set environment varialble : set KEY VALUE"

    def execute(self, args, context):
        if len(args) != 2:
            print("Usage: set KEY VALUE")
            return
        
        key, value = args
        context.env[key] = value

class EnvCommand(Command):
    name = "env"
    help = "Show all environment variables"

    def execute(self, args, context):
        if not context.env:
            print("No environment variable set")
            return
        
        for key,value in context.env.items():
            print(f"{key}={value}")




COMMANDS = {
    cmd.name : cmd for cmd in [
        HelpCommand(),
        ExitCommand(),
        EchoCommand(),
        DateCommand(),
        ClearCommand(),
        WhoAmICommand(),
        EnvCommand(),
        SetCommand()
    ]
}


def execute(cmd,args,context):
    if not cmd:
        return
    command = COMMANDS.get(cmd)
    if not command:
        print(f"Unknown Command: {cmd}")
        return
    command.execute(args,context)

    