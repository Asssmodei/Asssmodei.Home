memory = []
while True:
    a = int(input())
    if a < 0:
        break
    x = str(a)
    memory.append(x)
print(''.join(reversed(sorted(memory))))
