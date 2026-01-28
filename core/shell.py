from core.parser import parse
from core.executor import execute

class Shell:
    def run(self):
        while True:
            try:
                command = input("Kisan OS> ")
                cmd, args = parse(command)
                execute(cmd,args)
            except SystemExit:
                print("Goodbye 👋")
                break
            except KeyboardInterrupt:
                print("\nInterrupted ❌")
                break
