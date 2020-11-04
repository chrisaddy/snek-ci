import docker
from .config import Config


class Machine:
    def __init__(self, configuration):
        self.configuration = configuration
        self.client = docker.from_env()


    def start(self):
        print(self.client.configs.list())
        self.machine = self.client.containers.run(self.configuration.machine, detach=True)
        self.machine.logs()
        self.machine.start()

    def stop(self):
        self.machine.stop()

    def clean(self):
        self.machine.prune()
