"""Упражнение 9. Сложные проценты
(19 строк)
Представьте, что вы открыли в банке сберегательный счет под 4 % годо-
вых. Проценты банк рассчитывает в конце года и добавляет к сумме счета.
Напишите программу, которая запрашивает у пользователя сумму перво-
начального депозита, после чего рассчитывает и выводит на экран сумму
на счету в конце первого, второго и третьего годов. Все суммы должны
быть округлены до двух знаков после запятой.
"""


def deposit_request() -> float:
    deposit_amount = float(input("Введите сумму депозита: "))
    return deposit_amount


def percents_calculation(deposit: float, years: int, percent = 0.04) -> float:
    x = deposit
    y = percent
    for i in range(years):
        x += x * y
    return x


def info_output(deposit: float, func: callable, over_the_years: int = 50):
    y = over_the_years
    x = func(deposit, y)
    output_list = []
    for i in range(1, y+1):
        j = func(deposit,i)
        j = round(j, 2)
        output_list.append(j)
    output_dict = {x+1:y for x,y in enumerate(output_list)}
    result = ''
    for i in range(1, y+1):
        result = result + f'{i}) {output_dict[i]}\n'
    return result


print(info_output(deposit_request(), percents_calculation))
    
