class Fraction:
    def __init__(self, zn=1, ch=1):
        self.zn = zn
        self.ch = ch

    def inner(self):
        self.ch = int(input('Введите числитель '))
        self.zn = int(input('Введите знаменатель '))
        if self.zn == 0:
            raise ZeroDivisionError

    def __str__(self):
        return print(self.ch, '/', self.zn)
