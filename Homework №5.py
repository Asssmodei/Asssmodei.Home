def binarius(x, memory):
    memory = sorted(memory)
    f = True
    if x == memory[0]:
        return memory[0]
    elif x == memory[-1]:
        return memory[-1]
    elif x < memory[0] or x > memory[-1]:
        return None
    while f:
        print('Число больше или меньше чем', int(((memory[0] + memory[-1]) / 2)), '?')
        d = input()    # я спрашиваю у пользователя потому что программа изначально не знает число и типо угадывает
        if x == int((memory[0] + memory[-1]) / 2):
            return int((memory[0] + memory[-1]) / 2)
        elif d == 'больше':
            memory[0] = int((memory[0] + memory[-1]) / 2)
            f = True
        else:
            memory[-1] = int((memory[0] + memory[-1]) / 2)
            f = True
        z = int(((memory[0] + memory[-1]) / 2)) - x
        if z != 1 or z != -1:
            continue
        elif z == 1:
            return int(((memory[0] + memory[-1]) / 2)) - 1
        else:
            return int(((memory[0] + memory[-1]) / 2)) + 1
