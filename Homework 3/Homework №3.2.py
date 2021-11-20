def month(x):
    if x == 12 or (1 <= x <= 2):
        return "зима"
    elif 2 < x <= 5:   # Нормальная форма записи? Мне пайчарм так предлагает писать
        return 'весна'
    elif 6 <= x < 9:
        return "лето"
    elif 9 >= x and x < 12:
        return "осень"
    else:
        return None
