import math
from math import *


class Fraction:

    def __init__(self, ch: int = 0, zn: int = 1) -> None:
        self.zn = zn
        self.ch = ch

    def inner(self) -> None:
        self.ch = int(input('Введите числитель '))
        self.zn = int(input('Введите знаменатель '))
        if not self.zn:
            raise ZeroDivisionError

    def __str__(self) -> str:
        return f"{self.ch}/{self.zn}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other: "Fraction") -> bool:
        return self.ch == other.ch and self.zn == other.zn
    
    def __add__(self, other: 'Fraction') -> 'Fraction':
        k = self.__lcm(self.zn, other.zn)
        d = self.ch * (k // self.zn) + other.ch * (k // other.zn)
        return self.__class__(d, k)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        k = self.__lcm(self.zn, other.zn)
        d = self.ch * (k // self.zn) - other.ch * (k // other.zn)
        return self.__class__(d, k)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        k = self.ch * other.ch
        d = self.zn * other.zn
        return self.__class__(k, d)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        k = self.ch * other.zn
        d = self.zn * other.ch
        return self.__class__(k, d)

    def reduce(self) -> None:
        k = self.__gcd(self.zn, self.ch)
        # Знаменатель всегда должен быть положительным
        if self.zn < 0:
            self.ch = -self.ch
            self.zn = -self.zn
        self.zn = self.zn // k
        self.ch = self.ch // k

    def __lcm(self, a: int, b: int) -> int:
        return math.lcm(a, b)

    def __gcd(self, a: int, b: int) -> int:
        return math.gcd(a, b)


class IrreduceableFraction(Fraction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reduce()

    def inner(self, *args, **kwargs) -> None:
        super().inner()
        self.reduce()
        
