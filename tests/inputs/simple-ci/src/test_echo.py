from echo import echo

def test_echo_echoes():
    eko = echo("hello world")
    assert eko == "hello world"

