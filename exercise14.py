
"""Упражнение 14. Рост
(Решено. 16 строк)
Многие люди на планете привыкли рассчитывать рост человека в футах
и дюймах, даже если в их стране принята метрическая система. Напишите
программу, которая будет запрашивать у пользователя количество футов,
а затем дюймов в его росте. После этого она должна пересчитать рост
в сантиметры и вывести его на экран.
"""

def user_request() -> tuple:
    try:
        foot = float(input('Введите ваш рост в футах: '))
        inch = float(input('Введите остаток в дюймах: '))
        if foot <= 0 and inch <= 0:
            raise ValueError
    except ValueError:
        print('Некорректное значение')
        foot, inch = user_request()
    return foot, inch


def height_translator(height: tuple):
    foot, inch = height
    centimetrs = ((foot * 12) + inch) * 2.54
    print(f'Ваш рост: {centimetrs} см.')


while True:
    height_translator(user_request())
