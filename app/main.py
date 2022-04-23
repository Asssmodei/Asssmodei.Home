import math
from math import *


class Fraction:

    def __init__(self, ch: int = 0, zn: int = 1) -> None:
        self.zn = zn
        self.ch = ch

    def inner(self) -> None:
        self.ch = int(input('Введите числитель '))
        self.zn = int(input('Введите знаменатель '))
        if self.zn == 0:
            raise ZeroDivisionError

    def __str__(self) -> str:
        return f"{self.ch}/{self.zn}"

    def __eq__(self, other: "Fraction") -> bool:
        return self.ch == other.ch and self.zn == other.zn
    
    def __add__(self, other):
        k = self.__lcm(self.zn, other.zn)
        d = self.ch * (k // self.zn) + other.ch * (k // other.zn)
        return Fraction(d, k)

    def __sub__(self, other):
        k = math.lcm(self.zn, other.zn)
        d = self.ch * (k // self.zn) - other.ch * (k // other.zn)
        return Fraction(d, k)

    def __mul__(self, other):
        k = self.ch * other.ch
        d = self.zn * other.zn
        return Fraction(k, d)

    def __truediv__(self, other):
        k = self.ch * other.zn
        d = self.zn * other.ch
        return Fraction(k, d)

    def reduce(self) -> None:
        if self.ch == 0:
            return
        k = self.__gcd(self.zn, self.ch)
        self.zn = self.zn // k
        self.ch = self.ch // k

    def __lcm(self, a, b):
        return math.lcm(a, b)

    def __gcd(self, a, b):
        return math.gcd(a, b)


class IrreduceableFraction(Fraction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reduce()

    def inner(self, *args, **kwargs) -> None:
        super().inner()
        self.reduce()
        
