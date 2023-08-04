"""Упражнение 15. Расстояние
(20 строк)
Для этого упражнения вам необходимо будет написать программу, кото-
рая будет запрашивать у пользователя расстояние в футах. После этого
она должна будет пересчитать это число в дюймы, ярды и мили и вывес-
ти на экран. Коэффициенты для пересчета единиц вы без труда найдете
в интернете.
"""

def user_request():
    x = float(input('Введите футы: '))
    return x


def result_output(foots):
    dict_result = {'inch':foots * 12, 'miles':foots * 0.0001894,                    'yards':foots * 0.3333}

    print(foots, 'В других величинах:')
    for i in dict_result:
        print('      ',i,':',dict_result[i])


while True:
     result_output(user_request())
