def fibonacci(n):
    x = [0, 1]
    for i in range(2, n + 1):
        k = x[i-1] + x[i-2]
        x.append(k)
    print(x)
    return x
