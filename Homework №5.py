def binarius(x, memory):
    f = True
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
            return round((memory[0] + memory[-1]) / 2) - 1  # нам же дают упорядоченный список


assert binarius(1, [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 0  # выполнено
assert binarius(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4  # выполнено
assert binarius(7, [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 6  # выполнено
k = []
for i in range(1, 101):    # мне просто лень список на 100 писать
    k.append(i)
assert binarius(42, k) == 41  # выполенно
assert binarius(99, k) != 99  # выполнено
assert binarius(67, k) != 65  # выполнено
