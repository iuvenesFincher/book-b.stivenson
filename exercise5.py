"""
Упражнение 5. Сдаем бутылки
(Решено. 15 строк)
Во многих странах в стоимость стеклотары закладывается определенный
депозит, чтобы стимулировать покупателей напитков сдавать пустые бу-
тылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутыл-
ки большего объема – $0,25.
Напишите программу, запрашивающую у пользователя количество бу-
тылок каждого размера. На экране должна отобразиться сумма, которую
можно выручить, если сдать всю имеющуюся посуду. Отформатируйте
вывод так, чтобы сумма включала два знака после запятой и дополнялась
слева символом доллара.
"""


def request_from_user():
    try:
        small_bottles = int(input('Число бутылок объемом менее литра: '))
        large_bottles = int(input('Число бутылок объемом более литра: '))
    except ValueError:
        print('Введите целое число')
        small_bottles, large_bottles = request_from_user()
    return small_bottles, large_bottles


def sum_result(bootls_count: tuple):
    x = bootls_count[0] * 0.1 
    y = bootls_count[1] * 0.25
    return x + y

def output_from_user(result: float, rounding: int = 2, currency = '$'):
    correctly_result = round(result, rounding)
    return f'При сдаче можно выручить {correctly_result} {currency}!'


print(output_from_user(sum_result(request_from_user())))
