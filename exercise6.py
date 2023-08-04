"""
Упражнение 6. Налоги и чаевые
(Решено. 17 строк)
Программа, которую вы напишете, должна начинаться с запроса у поль-
зователя суммы заказа в ресторане. После этого должен быть произведен
расчет налога и чаевых официанту. Вы можете использовать принятую
в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
де программа должна отобразить отдельно налог, сумму чаевых и итог,
включая обе составляющие. Форматируйте вывод таким образом, чтобы
все числа отображались с двумя знаками после запятой.
"""


def user_request():
    try:
        money = float(input('Пожалуйста введите сумму вашего заказа: '))
    except ValueError:
        print('Введите число')
        money = user_request()
    if money < 0:
        print(' Введите положительное число')
        money = user_request()
    return money


def tax_tip_calculation(money: float, tax=0.05 , tip=0.18 ):
    tax_result = money * tax
    tip_result = money * tip
    return tax_result, tip_result


def output_from_user(final_counts: tuple):
    x = round(final_counts[0], 2)  # tax output
    y = round(final_counts[1], 2)  # tip output
    z = round(x + y, 2)  # tax and tip
    return f'Налог: {x}\nЧаевые: {y}\nИтог: {z}'


print(output_from_user(tax_tip_calculation(user_request())))
