"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
"""

import random


def bubble_sort(array):
    n = 1
    while n < len(array):
        is_sorted = True                                            # Улучшение заключается
        for i in range(len(array) - n):                             # в досрочном прекращении алгоритма
            if array[i] > array[i + 1]:                             # при достижении сортировки.
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1

    return array


array_ = [random.randint(-100, 99) for i in range(10)]
print(array_)
bubble_sort(array_)
print(array_)
