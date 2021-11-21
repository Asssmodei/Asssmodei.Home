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
        if x == (memory[0] + memory[-1]) / 2:
            return (memory[0] + memory[-1]) / 2
        elif x > (memory[0] + memory[-1]) / 2:
            memory[0] = (memory[0] + memory[-1]) / 2
            print(memory[0])
            f = True
        else:
            memory[-1] = (memory[0] + memory[-1]) / 2
            print(memory[-1])
            f = True
        z = ((memory[0] + memory[-1]) / 2) - x
        if -0.6 < z < 0.6:
            return round((memory[0] + memory[-1]) / 2)
