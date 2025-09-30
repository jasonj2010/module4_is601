import pytest
from app.operation import Operations

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (2.5, 2.5, 5.0),
])
def test_add(a, b, expected):
    assert Operations.add(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Operations.divide(1, 0)

def test_divide_normal():
    assert Operations.divide(6, 3) == 2
