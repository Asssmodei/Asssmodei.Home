print('Введите выражение')
ways = input()
a = ways.count('(') - ways.count(')')
if a < 0:
    print('Не хватает открывающих скобки', -a)
elif a > 0:
    print('Не хватает закрывающих скобок', a)
