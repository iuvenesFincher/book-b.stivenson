﻿
"""EXERCISE19   
Упражнение 19. Свободное падение
(Решено. 15 строк)
Напишите программу для расчета скорости объекта во время его сопри-
косновения с землей. Пользователь должен задать высоту в метрах, с ко-
торой объект будет отпущен. Поскольку объекту не будет придаваться
ускорение, примем его начальную скорость за 0 м/с. Предположим, что
ускорение свободного падения равно 9,8 м/с2. При известных начальной
скорости (vi), ускорении (a) и дистанции (d) можно вычислить скорость
при соприкосновении объекта с землей по формуле
""" 
import math


def main():
    height = float(input('Введите высоту: '))
    v = 0
    a = 9.8
    result_velocity = math.sqrt(v ** 2 + 2 * a * height)
    print(result_velocity) 


while True:
    try:
        main()
    except ValueError:
        print('Некорректное значение')
