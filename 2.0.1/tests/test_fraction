from app.main import Fraction, IrreduceableFraction


def test_eq():
    assert Fraction(2, 1) == Fraction(2, 1)


def test_not_eq():
    assert Fraction(3, 2) != Fraction(2, 2)


def test_reduce():
    q = Fraction(2, 4)
    q.reduce()
    assert q == Fraction(1, 2)


def test_inner(mocker):
    mocker.patch('builtins.input', side_effect=['1', '2'])
    f = Fraction()
    f.inner()
    assert f == Fraction(1, 2)
