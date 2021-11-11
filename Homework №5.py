def binarius(x, memory):
    memory = sorted(memory)
    f = True
    if x < memory[0] or x > memory[-1]:
        return None
    while f:
        z = ((memory[0] + memory[-1]) / 2) - x
        print('Число больше или меньше чем', z, '?')
        d = input()    # я спрашиваю у пользователя потому что программа изначально не знает число и типо угадывает
        if d == 'больше':
            memory[0] = (memory[0] + memory[-1]) / 2
            f = True
        else:
            memory[-1] = (memory[0] + memory[-1]) / 2
            f = True
        if z != 1 or z != -1:
            continue
        elif z == 1:
            return ((memory[0] + memory[-1]) / 2) - 1
        else:
            return (memory[0] + memory[-1]) / 2 + 1

