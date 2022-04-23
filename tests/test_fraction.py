def test_add(a, b, c):
    assert a + b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'),
    [[Fraction(-2, 5), Fraction(3, 5), Fraction(-5, 5)],
     [Fraction(11, -6), Fraction(2, 3), Fraction(-15, 6)],
     [Fraction(2, -2), Fraction(1, -2), Fraction(-1, 2)]
     ]
)
def test_sub(a, b, c):
    print(a - b)
    assert a - b == c



def test_mul():
    a = Fraction(3, 4)
    b = Fraction(2, 5)
    assert a * b == Fraction(6, 20)


def test_truediv():
    a = Fraction(3, 4)
    b = Fraction(2, 2)
    assert a / b == Fraction(6, 8)
