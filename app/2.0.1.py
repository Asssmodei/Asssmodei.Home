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

    def inner(self, *args, **kwargs) -> None:
        super().inner()
        self.reduce()
        
