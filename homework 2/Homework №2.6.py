print('Введите строку')
a = input()
x = []
for i in a:
    if i.isdigit():
        x.append(i)
print('Какой элемент ищем?')
k = int(input())
print(x[k - 1])
