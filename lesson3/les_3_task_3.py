# В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

array = [random.randint(-100, 100) for i in range(10)]
print(array)

min_ = 0
max_ = 0
for i in range(len(array)):
    if array[i] < array[min_]:
        min_ = i
    elif array[i] > array[max_]:
        max_ = i
print(f'Min = {array[min_]} в ячейке {min_}')
print(f'Max = {array[max_]} в ячейке {max_}')

array[min_], array[max_] = array[max_], array[min_]
print(array)
