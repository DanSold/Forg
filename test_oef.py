from oef import name_processing, age_processing

def test_name_valid_already_formatted():
    assert name_processing("Dan") == "Dan"

def test_name_formatting_needed():
    assert name_processing("dAN") == "Dan"
    assert name_processing("DAN") == "Dan"
    assert name_processing("dan") == "Dan"

def test_name_too_short_then_valid(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "Anna")
    result = name_processing("A")
    assert result == "Anna"
    captured = capsys.readouterr()
    assert "Your name is too short" in captured.out