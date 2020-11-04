import yaml
from snek.machine import Machine
from snek.config import Config

with open("tests/inputs/simple-ci/.snek-ci.yml", "r") as f:
    config = yaml.load(f, yaml.FullLoader)

config = Config(config)

machine = Machine(config)
machine.start()
machine.stop()
machine.clean()
