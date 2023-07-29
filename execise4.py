"""
Упражнение 4. Площадь садового участка
(Решено. 15 строк)
Создайте программу, запрашивающую у пользователя длину и ширину
садового участка в футах. Выведите на экран площадь участка в акрах.
"""


def request():
    try:
        x = float(input('Введите ширину участка в футах: '))
        y = float(input('Введите высоту участка в футах: '))
    except ValueError:
        print('Введите корректное значение')
        x, y = request()
    
    return x, y


def metering_in_akre(metering: tuple):
    result = 1
    for i in metering: result *= i
    return f'{result/43560} акров >> площадь участка'


print(metering_in_akre(request()))    
