def alot(x):
    q = 0.
    for i in x:
        q += x[i]
    print('Среднее арифметическое равно ', q/len(x))
