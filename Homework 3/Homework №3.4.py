def counter():
    x = []
    while True:
        a = input()
        if a == '':
            break
        x.append(a)
        for i in set(x):
            y = x.count(i)
            print('Элемент', i, '\t', '|', '\t',  'частота - ', y)
