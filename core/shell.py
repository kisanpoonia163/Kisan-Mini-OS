from core.parser import parse
from core.executor import execute
from core.context import Context

class Shell:
    def __init__(self):
        self.context = Context()

    def run(self):
        while self.context.running:
            try:
                command = input("Kisan OS> ")
                cmd, args = parse(command)
                execute(cmd,args,self.context)
            except KeyboardInterrupt:
                print("\nInterrupted")
                break
