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
        if -0.51 < z < 0.51:
            print(round((memory[0] + memory[-1]) / 2))
            return round((memory[0] + memory[-1]) / 2)


assert binarius(1, [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 1  # выполнено
assert binarius(5, [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 5 # выполнено
assert binarius(7, [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 7  # выполнено
k = []
for i in range(1, 101):    # мне просто лень список на 100 писать
    k.append(i)
assert binarius(42, k) == 42  # выполенно
assert binarius(99, k) == 99  # выполнено
assert binarius(99, k) == 100  # не выполнено
assert binarius(67, k) == 66  # не выполнено
