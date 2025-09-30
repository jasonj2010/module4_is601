import pytest
from app.calculation import Calculation, CalculationFactory, CalculationHistory

def test_calculation_perform_add():
    c = Calculation(lambda a,b: a+b, 2, 3)
    assert c.perform() == 5

def test_factory_create_valid():
    c = CalculationFactory.create("add", 2, 3)
    assert c.perform() == 5

@pytest.mark.parametrize("op", ["add","subtract","multiply","divide"])
def test_factory_each_op(op):
    c = CalculationFactory.create(op, 4, 2)
    assert isinstance(c, Calculation)

def test_factory_unknown_op():
    with pytest.raises(ValueError):
        CalculationFactory.create("nope", 1, 2)

def test_history_add_and_str():
    CalculationHistory.history.clear()
    c = CalculationFactory.create("add", 1, 1)
    CalculationHistory.add(c)
    assert len(CalculationHistory.history) == 1
    s = str(CalculationHistory.history[0])
    assert "add" in s and "= 2" in s
