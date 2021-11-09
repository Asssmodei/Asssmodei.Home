def binarius():
    x = int(input())  # загаданное число
    a, b = int(input())  # границы
    f = True
    while f:
        print('Число больше или меньше чем', (a + b) / 2, '?')
        d = input()
        print('Число больше или меньше на 1?')
        q = input()
        if d == 'больше':
            a = (a + b) / 2
            f = True
        else:
            b = (a + b) / 2
            f = True
        if q == 'нет':
            continue
        elif q == 'Больше':
            z = (a + b) / 2 + 1
            f = False
        else:
            z = (a + b) / 2 - 1
            f = False
    if z == x:
        print('УРА')
