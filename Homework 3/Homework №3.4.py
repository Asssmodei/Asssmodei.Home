from Homework31 import print_string


def counter():
    x = print_string()
    for i in set(x):
        y = x.count(i)
        print('Элемент', i, '\t', '|', '\t',  'частота - ', y)


counter()
