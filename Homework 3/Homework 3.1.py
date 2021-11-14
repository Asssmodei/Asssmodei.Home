def print_string():
    list1 = []
    while True:
        x = input()
        if x == "":
            break
        else:
            list1.append(x)
    s = list1[0]
    for i in range(1, len(list1)-1):
        s += " " + list1[i]
    print(s)
