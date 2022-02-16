class Fraction:
    def __init__(self, zn=1, ch=1):
        self.zn = zn
        self.ch = ch

    def inner(self):
        self.ch = float(input('Введите числитель '))
        self.zn = float(input('Введите знаменатель '))
        if self.zn == 0:
            raise ZeroDivisionError
        elif int(self.ch) != float(self.ch):
            exit()

    def __str__(self):
        return print(int(self.ch), '/', int(self.zn))
