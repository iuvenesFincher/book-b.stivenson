﻿"""EXERCISE17   
Упражнение 17. Теплоемкость
(Решено. 23 строки)
Количество энергии, требуемое для повышения температуры одного
грамма материала на один градус Цельсия, называется удельной тепло-
емкостью материала и обозначается буквой C. Общее количество энергии
(q), требуемое для повышения температуры m граммов материала на ΔT
градусов Цельсия, может быть рассчитано по формуле:
q = mCDT.
Напишите программу, запрашивающую у пользователя массу воды
и требуемую разницу температур. На выходе вы должны получить коли-
чество энергии, которое необходимо добавить или отнять для достижения
желаемого температурного изменения.
Подсказка. Удельная теплоемкость воды равна 4,186 Дж
г·С. Поскольку вода обладает
плотностью 1 грамм на миллилитр, в данном упражнении можно взаимозаменять
граммы и миллилитры.
Расширьте свою программу таким образом, чтобы выводилась так-
же стоимость сопутствующего нагрева воды. Обычно принято измерять
элект ричество в кВт·ч, а не в джоулях. Для данного примера предположим,
что электричество обходится нам в 8,9 цента за один кВт·ч. Используйте
свою программу для подсчета стоимости нагрева одной чашки кофе.
Подсказка. Для решения второй части задачи вам придется найти способ перевода
единиц электричества между джоулями и кВт·ч.
""" 


def get_joule() -> float:
    t = float(input("Введите необходимую разницу температуры: "))
    m = float(input("Введите массу воды в граммах: "))
    C = 4.186
    q = t * m * C
    return q


def get_price(joule, energy_cost: float = 0.089) -> str:
    q = joule
    watt = q / 3_600_000
    price = watt * energy_cost
    return f'Стоимость нагрева будет равна: {price}'


def main():
    x = get_joule()
    print(get_price(x))


while True:
    main()
    
