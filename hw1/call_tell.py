x = float(input('Введите код города\n'))
time = float(input('Введите время переговоров\n'))

def price(x, time):
    if x == 343:
        return 15 * time
    elif x == 381:
        return 18 * time
    elif x == 473:
        return 13 * time
    elif x == 485:
        return 11 * time
    else:
        return 'Я не знаю такого города'


print(price(x, time))