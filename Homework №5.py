def binarius(memory, x):
    f = True
    num = int
    position = 0
    if memory == []:
        return None
    elif x < memory[0] or x > memory[-1]:
        return None
    elif x == memory[0]:
        return 0
    elif x == memory[-1]:
        return len(memory) - 1
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


assert binarius([], 42) is None                       # выполнено
assert binarius([0], 0) == 0                         # выполнено
assert binarius([0], 1) is None                      # выполнено
assert binarius([-1, 0, 42], 0) == 1                     # выполнено
assert binarius([-6, -5, -4, -3, -2, -1], -4) == 2         # выполнено
assert binarius([1, 2, 3, 4, 5, 6], 4) == 3                  # выполнено
assert binarius([1, 2, 3, 4, 5, 6, 7], 4) == 3               # выполнено
assert binarius([1, 2, 3, 4, 5], 7) is None              # выполнено
assert binarius([1, 2, 3, 4, 5, 6], 7) is None          # выполнено
assert binarius([-42, 0, 42], 42) == 2                  # выполнено
assert binarius([42, 42, 42, 42, 42], 42) == 0          # выполнено
assert binarius([-42, -42, -42, -42, -42], -42) == 0        # выполнено
assert binarius([42, 42, 42, 42, 43], 43) == 4          # выполнено
assert binarius([41, 42, 42, 42, 42], 41) == 0          # выполнено
assert binarius([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2       # выполнено
assert binarius([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4        # выполнено
