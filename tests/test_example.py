from dogmatica import greet


def test_greet():
    assert greet("Codex") == "Hello, Codex!"
