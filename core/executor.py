def execute(cmd,args):
    if cmd == "help":
        print("Available Commands : help, exit")
    elif cmd == "exit":
        raise SystemExit
    else:
        print(f"Unknown Command: {cmd}")