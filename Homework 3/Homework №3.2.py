def month(x):
    if x == 12 and x <= 2:
        return "зима"
    elif 2 < x < 6:
        return 'весна'
    elif 6 <= x < 9:
        return "лето"
    elif 9 <= x < 12:
        return "осень"


print(month(2))
