def binarius(x, memory: object):
    f = True
    num = int
    position = 0
    if x == memory[0]:
        print(memory[0])
        return memory[0] - 1
    elif x == memory[-1]:
        print(memory[-1])
        return memory[-1] - 1
    elif x < memory[0] or x > memory[-1]:
        return None
    elif memory == []:
        return None
    while f:
        if x == (memory[0] + memory[-1]) / 2:
            return ((memory[0] + memory[-1]) / 2) - 1
        elif x > (memory[0] + memory[-1]) / 2:
            memory[0] = (memory[0] + memory[-1]) / 2
            print(memory[0])
            f = True
        else:
            memory[-1] = (memory[0] + memory[-1]) / 2
            print(memory[-1])
            f = True
        z = ((memory[0] + memory[-1]) / 2) - x
        if -0.51 < z < 0.51:
            print(round((memory[0] + memory[-1]) / 2))
            num = round((memory[0] + memory[-1]) / 2)
            f = False
    for i in memory:
        print(i)
        if i == num:
            return position
        position += 1


assert binarius(12, [1, 12, 12, 21]) == 1  # работает
k = []
for i in range(1, 101):  # мне просто лень список на 100 писать
    k.append(i)
assert binarius(22, k) == 21  # работает
assert binarius() == None  # работает
