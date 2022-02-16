class Fraction:
    def __init__(self, zn=1, ch=1):
        self.zn = zn
        self.ch = ch

    zn = float
    ch = float

    def inner(self):
        self.ch = float(input())
        self.zn = float(input())
        if self.zn == 0:
            raise ZeroDivisionError
        elif int(self.ch) != float(self.ch):
            exit()

    def __str__(self):
        return print(self.ch, '/', self.zn)
