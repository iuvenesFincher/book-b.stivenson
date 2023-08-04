"""Упражнение 11. Потребление топлива
(13 строк)
В США потребление автомобильного топлива исчисляется в милях на
галлон (miles-per-gallon – MPG). В то же время в Канаде этот показатель
обычно выражается в литрах на 100 км (liters-per-hundred kilometers –
L/100 km). Используйте свои исследовательские способности, чтобы опре-
делить формулу перевода первых единиц исчисления в последние. После
этого напишите программу, запрашивающую у пользователя показатель
потребления топлива автомобилем в американских единицах и выводя-
щую его на экран в канадских единицах.
"""


def mpg_per_kpl(miles_and_galons: tuple) -> tuple:
    miles = miles_and_galons[0]
    galons = miles_and_galons[1]
    kilometers = miles * 1.61
    liters = galons * 3.78541   
    return kilometers, liters


def str_kpl(kilometers_and_liters: tuple) -> str:
    kilometers = kilometers_and_liters[0]
    liters = kilometers_and_liters[1]
    result = kilometers / liters
    result_str = f"{result} км/л"
    return result_str


while True:
    try:
        x = float(input('Введите количество милей на 1 галлон: '))
        if x <= 0:
            raise ValueError
    except ValueError:
        print('Введите число больше 0')
    y = 1
    print(str_kpl(mpg_per_kpl((x,y))))
