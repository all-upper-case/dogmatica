from dogmatica import codex_playground


def test_codex_playground_defaults():
    playground = codex_playground()

    assert playground["name"] == "Codex Playground"
    assert playground["owner"] == "Codex"
    assert "experiments" in playground["description"]
