import threading

class Job:
    def __init__(self, pid, target):
        self.pid = pid
        self.thread = threading.Thread(target=target)
        self.running = False

    def start(self):
        self.running = True
        self.thread.start()

    def is_alive(self):
        return self.thread.is_alive()
