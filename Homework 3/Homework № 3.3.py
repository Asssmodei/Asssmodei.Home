def fibonacci(n):
    x = []
    x[0] = 0
    x[1] = 1
    for i in range(2, n):
        x[i] = x[i-1] + x[i-2]
    return x
