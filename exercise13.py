"""Упражнение 13. Размен
(Решено. 35 строк)
Представьте, что вы пишете программное обеспечение для автомати-
ческой кассы в магазине самообслуживания. Одной из функций, зало-
женных в кассу, должен быть расчет сдачи в случае оплаты покупателем
наличными.
Напишите программу, которая будет запрашивать у пользователя сум-
му сдачи в центах. После этого она должна рассчитать и вывести на экран,
сколько и каких монет потребуется для выдачи указанной суммы, при ус-
ловии что должно быть задействовано минимально возможное количест-
во монет. Допустим, у нас есть в распоряжении монеты достоинством в 1,
5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.
"""


def user_request() -> float:
    try:
        change = float(input("Введите сдачу: "))
        if change <= 0:
            print('Сдача меньше или = 0')
            raise ValueError
    except ValueError:
        print('Некорректное значение')
        change = user_request()
    return change

def coin_counter(change: float) -> dict:
    dict_result = {
                   '1': 0, '5': 0, '10': 0, '25': 0, 
                   'loonie': 0, 'toonie': 0
                  }
    while change >= 200:
        change -= 200
        dict_result['toonie'] += 1
    while change >= 100:
        change -= 100
        dict_result['loonie'] += 1
    while change >= 25:
        change -= 25
        dict_result['25'] += 1
    while change >= 10:
        change -= 10
        dict_result['10'] += 1
    while change >= 5:
        change -= 5
        dict_result['5'] += 1
    while change >= 1:
        change -= 1
        dict_result['1'] += 1
    return dict_result


def result_output(money_dict:dict) -> str:
    for i in money_dict:
        print([i], ':', money_dict[i])

while True:
    result_output(coin_counter(user_request()))
    

    
