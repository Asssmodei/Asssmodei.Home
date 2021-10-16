print('Введите строку')
a = list(input())
x = []
for i in range(0, len(a)):
    if a[i].isdigit():
        x.append(a[i])
print('Какой элемент ищем?')
k = int(input())
print(x[k - 1])