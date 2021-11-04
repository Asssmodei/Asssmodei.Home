def alot():
    x = []
    a = True
    while a:
        b = float(input())
        x.append(b)
        print('Хотите ввести еще 1 число?')
        g = input('Введите да или нет')
        if g == 'Да':
            a = True
        else:
            a = False
    q = 0.
    for i in x:
        q += x[i]
    print('Среднее арифметическое равно ', q/len(x))
