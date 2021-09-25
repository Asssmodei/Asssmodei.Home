memory = []
for i in range(1, 5):
    memory[i] = int(input())
    if memory[i] < 10:
        continue
    else:
        break
        print('Введено число больше 10')
    print('\n', memory[i])
