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
    
    def __eq__(self, other: "Fraction") -> bool:
        return self.ch == other.ch and self.zn == other.zn    

    def reduce(self) -> None:
        if self.ch == 0:
            return
        k = gcd(self.zn, self.ch)
        self.zn = self.zn // k
        self.ch = self.ch // k
  
       
class IrreduceableFraction(Fraction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reduce()

    
s = IrreduceableFraction(4, 2)
a = IrreduceableFraction(2, 1)

assert s == a
    
s = IrreduceableFraction(4, 2)
a = IrreduceableFraction(0, 2)

assert s == a
       
