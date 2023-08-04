"""
Упражнение 7. Сумма первых n положительных чисел
(Решено. 11 строк)
Напишите программу, запрашивающую у пользователя число и подсчи-
тывающую сумму натуральных положительных чисел от 1 до введенного
пользователем значения. Сумма первых n положительных чисел может
быть рассчитана по формуле: sum = (n)(n+1)/2
"""


def request():
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print('Некорректное значение')
        number = request()
    if number <= 0:
        print('Введите число от 1')
        number = request()
    return number


def calculation(number: int):
    x = number
    result = (x)*(x+1)/2
    return result


print(calculation(request()))    
