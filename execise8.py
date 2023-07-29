"""
Упражнение 8. Сувениры и безделушки
(15 строк)
Интернет-магазин занимается продажей различных сувениров и безде-
лушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите про-
грамму, запрашивающую у пользователя количество тех и других покупок,
после чего выведите на экран общий вес посылки.
"""


def request():
    try:
        souvenirs_quantity = int(input('Число сувениров: '))
        bauble_quantity = int(input('Число безделушек: '))
    except ValueError:
        print('Число введите')
        souvenirs_quantity, bauble_quantity = request()
    if bauble_quantity < 0 or souvenirs_quantity < 0:
        print('Нельзя вводить отрицательное')
        souvenirs_quantity, bauble_quantity = request()
    return souvenirs_quantity, bauble_quantity


def weight_calculation(quantity: tuple):
    x = quantity[0] * 75
    y = quantity[1] * 112
    return x + y


def result_output(weight: int):
    x = weight
    return f'Общий вес посылки: {x} гр.'


while True:
    print(result_output(weight_calculation(request())))
