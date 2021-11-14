def counter():
    a = []
    while True:
        while True:
            x = input()
            if x == "":
                break
            else:
                a.append(x)
        for i in set(a):
            y = a.count(i)
            print('Элемент', i, '\t', '|', '\t',  'частота - ', y)
