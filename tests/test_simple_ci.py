import pytest
import yaml
from snek.config import Config

with open("tests/inputs/simple-ci/.snek-ci.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def test_config_has_name():
    assert "name" in config
    assert isinstance(config["name"], str)
    assert len(config["name"]) >= 1


def test_config_has_build():
    assert "build" in config
    assert isinstance(config["build"], list)
    assert len(config["build"]) >= 1


def test_missing_name_throws_exception():
    with open("tests/inputs/malformed-ci/missing-name/.snek-ci.yml", "r") as f:
        config_file = yaml.load(f, Loader=yaml.FullLoader)

    with pytest.raises(KeyError):
        config = Config(config_file)
        config = config.validate()


def test_missing_build_throws_exception():
    with open("tests/inputs/malformed-ci/missing-build/.snek-ci.yml", "r") as f:
        config_file = yaml.load(f, Loader=yaml.FullLoader)

    with pytest.raises(KeyError):
        config = Config(config_file)
        config = config.validate()


def test_build_is_list():
    with open("tests/inputs/malformed-ci/build-not-list/.snek-ci.yml", "r") as f:
        config_file = yaml.load(f, Loader=yaml.FullLoader)

    with pytest.raises(ValueError):
        config = Config(config_file)
        config = config.validate()

