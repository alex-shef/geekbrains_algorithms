"""
3. Массив размером 2m + 1, где m — натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
"""

from random import randint
import numpy

m = int(input('Введите натуральное число: '))
array_ = [randint(1, 100) for _ in range(2*m+1)]
print(f'Изначальный массив - {array_}')


def median(array, k=len(array_)/2):
    """
    Алгоритм быстрого выбора (quickselect) Хоара
    """
    if len(array) == 1:
        return array[0]
    else:
        pivot = array[0]    # Можно выбрать любой элемент

        below_pivot_array = [elem for elem in array if elem < pivot]
        above_pivot_array = [elem for elem in array if elem > pivot]
        pivot_array = [elem for elem in array if elem == pivot]

        if k < len(below_pivot_array):
            return median(below_pivot_array, k)
        elif k < len(below_pivot_array) + len(pivot_array):
            return pivot_array[0]
        else:
            return median(above_pivot_array, k - len(below_pivot_array) -
                          len(pivot_array))


median_ = median(array_)
print(f'Медиана массива - {median_}')
print(f'Медиана массива через модуль numpy - {numpy.median(array_)}')
