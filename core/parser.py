def parse(command: str):
    parts = command.strip().split()
    if not parts:
        return None, []
    return parts[0], parts[1:]