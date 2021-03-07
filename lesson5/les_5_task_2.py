"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’,‘F’,‘1’], произведение - [‘7’,‘C’,‘9’,‘F’,‘E’].
"""

from collections import deque
from copy import copy

HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
           'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
           8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
           15: 'F'}

x = deque(input('1-е число: ').upper())
y = deque(input('2-е число: ').upper())


def hex_sum(a=copy(x), b=copy(y)):
    hex_deque = deque()
    in_mind = 0
    result = ''

    if len(a) < len(b):                                     # добавление нулей, если разное кол-во цифр в числах
        a.extendleft('0' * (len(b) - len(a)))
    elif len(a) > len(b):
        b.extendleft('0' * (len(a) - len(b)))

    for i in range(len(a) - 1, -1, -1):                     # "перевод" в 10-ую систему и сложение
        hex_deque.append(HEX_NUM[a[i]] + HEX_NUM[b[i]])

    for elem in hex_deque:                                  # "перевод" в 16-ую систему
        if elem + in_mind > 15:
            result = result + HEX_NUM[elem + in_mind - 16]
            in_mind = 1
        else:
            result = result + HEX_NUM[elem + in_mind]
            in_mind = 0
    if in_mind == 1:
        result = result + '1'

    return result[::-1]


def hex_multiple(c=copy(x), d=copy(y)):
    hex_deque = deque()
    hex_list = []
    in_mind = 0
    result = ''

    if len(c) < len(d):                                      # для удобства умножения
        c, d = d, c

    for j in range(len(d) - 1, -1, -1):                      # "перевод" в 10-ую систему и умножение
        for i in range(len(c) - 1, -1, -1):
            hex_deque.append(HEX_NUM[c[i]] * HEX_NUM[d[j]])
        hex_list.append(hex_deque)
        hex_deque = deque()

    for i, elem in enumerate(hex_list):                      # добавление нулей для сложения
        if i == 0:
            elem.extend([0] * (len(hex_list) - 1))
        elif i == len(hex_list) - 1:
            elem.extendleft([0] * (len(hex_list) - 1))
        else:
            elem.extendleft([0] * i)
            elem.extend([0] * (len(hex_list) - 1 - i))

    result_list = [0 for _ in range(len(hex_list[0]))]       # список для сложения

    for elem in hex_list:                                    # сложение
        for i in range(len(elem)):
            result_list[i] += elem[i]

    for elem in result_list:                                 # "перевод" в 16-ую систему(по сути повторяющийся кусок кода,
        if elem + in_mind > 15:                              #  можно вывести как отдельную функцию)
            result = result + HEX_NUM[(elem + in_mind) % 16]
            in_mind = (elem + in_mind) // 16
        else:
            result = result + HEX_NUM[elem + in_mind]
            in_mind = 0
    if in_mind != 0:
        result = result + str(in_mind)

    return result[::-1]


print(hex_sum())
print(hex_multiple())
