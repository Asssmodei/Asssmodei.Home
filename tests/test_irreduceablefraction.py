from app.main import Fraction, IrreduceableFraction


def test_irreduceable():
    q = IrreduceableFraction(2, 4)
    assert q == Fraction(1, 2)
