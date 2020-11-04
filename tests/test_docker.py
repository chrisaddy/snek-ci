import yaml


with open("tests/inputs/simple-ci/.snek-ci.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
