print('Введите выражение')
ways = input()
a = ways.count('(') - ways.count(')')
if a < 0:
    print('Не хватает открывающих скобки')
elif a > 0:
    print('Не хватает закрывающих скобок')
else:
    print('Проблем со скобками нету')
