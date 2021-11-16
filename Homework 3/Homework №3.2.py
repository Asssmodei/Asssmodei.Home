def month(x):
    if x == 12 or (1 <= x < 2):
        return "зима"
    elif x > 2 and x < 6:
        return 'весна'
    elif x >= 6 and x < 9:
        return "лето"
    elif 9 >= x and x < 12:
        return "осень"
    else:
        return None
