

class Config:
    def __init__(self, config):
        self.config = config
        self.machine = config.get("machine")

    def validate(self):
        if "name" not in self.config:
            print("config missing name key")
            raise KeyError
        if "build" not in self.config:
            print("config missing build key")
            raise KeyError
        if not isinstance(self.config["build"], list):
            print(f"expecting build to be a list, got {type(self.config['build'])}")
            raise ValueError
