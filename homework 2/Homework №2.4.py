print('Введите выражение')
ways = input()
if ways.count('(') < ways.count(')'):
    print('Не хватает открывающих скобки')
elif ways.count('(') > ways.count(')'):
    print('Не хватает закрывающих скобок')

