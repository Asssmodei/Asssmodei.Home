from math import *


class Fraction:

    def __init__(self, zn: int = 1, ch: int = 0) -> None:
        self.zn = zn
        self.ch = ch

    def inner(self) -> None:
        self.ch = int(input('Введите числитель '))
        self.zn = int(input('Введите знаменатель '))
        if self.zn == 0:
            raise ZeroDivisionError

    def __str__(self) -> str:
        return f"{self.ch}/{self.zn}"

    def reduce(self) -> str:
        k = gcd(self.zn, self.ch)
        return f"{(self.zn / k)}/{(self.zn / k)}"


s = Fraction()
s.inner()
s.__str__()
s.reduce()
