"""EXERCISE18   
Объем цилиндра может быть рассчитан путем умножения площади круга,
лежащего в его основе, на высоту. Напишите программу, в которой поль-
зователь будет задавать радиус цилиндра и его высоту, а в ответ получать
его объем, округленный до одного знака после запятой.

"""


import math


def main():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))
    area = math.pi * radius ** 2
    volume = area * height
    volume = round(volume, 1)
    return f'Объем цилиндра: {volume}'


while True:
    try:
        print(main())
    except ValueError:
        print('Некорректное значение')
