from app.main import IrreduceableFraction


def test_irreduceable():
    q = IrreduceableFraction(2, 4)
    assert q == IrreduceableFraction(1, 2)


def test_inner(mocker):
    mocker.patch('builtins.input', side_effect=['5', '10'])
    f = IrreduceableFraction()
    f.inner()
    assert f == IrreduceableFraction(1, 2)


def test_add():
    a = IrreduceableFraction(2, 4)
    b = IrreduceableFraction(4, 6)
    assert a + b == IrreduceableFraction(7, 6)


def test_sub():
    a = IrreduceableFraction(2, 2)
    b = IrreduceableFraction(1, 2)
    assert a - b == IrreduceableFraction(1, 2)


def test_mul():
    a = IrreduceableFraction(2, 4)
    b = IrreduceableFraction(1, 5)
    assert a * b == IrreduceableFraction(1, 10)


def test_truediv():
    a = IrreduceableFraction(4, 2)
    b = IrreduceableFraction(5, 3)
    assert a / b == IrreduceableFraction(6, 10)
