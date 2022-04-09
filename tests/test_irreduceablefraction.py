from app.main import IrreduceableFraction


def test_irreduceable():
    q = IrreduceableFraction(2, 4)
    assert q == IrreduceableFraction(1, 2)


def test_inner(mocker):
    mocker.patch('builtins.input', side_effect=['5', '10'])
    f = IrreduceableFraction()
    f.inner()
    assert f == IrreduceableFraction(1, 2)
    
