from app.main import Fraction
import pytest


a = ([Fraction(1, 1), Fraction(1, 1)])
b = ([Fraction(-1, 1), Fraction(1, 1)])
c = ([Fraction(1, -1), Fraction(-1, 1)])
d = ([Fraction(-1, 1), Fraction(-1, 1)])
e = ([Fraction(-1, -1), Fraction(-1, -1)])


def test_eq():
    assert Fraction(2, 1) == Fraction(2, 1)


def test_not_eq():
    assert Fraction(3, 2) != Fraction(2, 2)


def test_reduce():
    q = Fraction(2, -4)
    q.reduce()
    assert q == Fraction(-1, 2)


def test_inner(mocker):
    mocker.patch('builtins.input', side_effect=['1', '2'])
    f = Fraction()
    f.inner()
    assert f == Fraction(1, 2)


def test_str():
    q = Fraction(1, 2)
    assert str(q) == '1/2'


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(2, 1)],
        [*b, Fraction(0, 1)],
        [*c, Fraction(-2, 1)],
        [*d, Fraction(-2, 1)],
        [*e, Fraction(2, 1)]
    ])
def test_add(a, b, c):
    assert a + b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(0, 1)],
        [*b, Fraction(-2, 1)],
        [*c, Fraction(0, 1)],
        [*d, Fraction(0, 1)],
        [*e, Fraction(0, 1)]
    ])
def test_sub(a, b, c):
    assert a - b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(1, 1)],
        [*b, Fraction(-1, 1)],
        [*c, Fraction(-1, -1)],
        [*d, Fraction(1, 1)],
        [*e, Fraction(1, 1)]
    ])
def test_mul(a, b, c):
    assert a * b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(1, 1)],
        [*b, Fraction(-1, 1)],
        [*c, Fraction(1, 1)],
        [*d, Fraction(-1, -1)],
        [*e, Fraction(1, 1)]
    ])
def test_truediv(a, b, c):
    assert a / b == c
