import builtins
from app.calculator import calculator

def run_repl(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(it))
    calculator()

def test_help_and_exit(monkeypatch, capsys):
    run_repl(monkeypatch, ["help", "exit"])
    out, _ = capsys.readouterr()
    assert "Commands:" in out and "Goodbye!" in out

def test_add_and_history(monkeypatch, capsys):
    run_repl(monkeypatch, ["add", "2", "3", "history", "exit"])
    out, _ = capsys.readouterr()
    assert "Result: 5.0" in out
    assert "add" in out

def test_generic_exception_path(monkeypatch, capsys):
    import app.calculator as ui

    def boom(*_args, **_kwargs):
        raise RuntimeError("boom")

    # when calculator() calls CalculationFactory.create, it will raise
    monkeypatch.setattr(ui.CalculationFactory, "create", boom)
    run_repl(monkeypatch, ["add", "2", "3", "exit"])
    out, _ = capsys.readouterr()
    assert "Invalid command. Type 'help' for options." in out

def test_valueerror_non_numeric_operands(monkeypatch, capsys):
    # "add" then non-numeric "a" triggers ValueError -> prints "Error: ...", then exit
    run_repl(monkeypatch, ["add", "a", "exit"])
    out, _ = capsys.readouterr()
    assert "Error:" in out
