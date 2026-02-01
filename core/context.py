class Context:
    def __init__(self):
        self.env = {}
        self.running = True
        self.version = "0.3"
        self.job = {}
        self.next_pid = 1