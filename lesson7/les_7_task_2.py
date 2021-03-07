"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge(first, second):
    res = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            res.append(first[i])
            i += 1
        else:
            res.append(second[j])
            j += 1
    res += first[i:] + second[j:]
    return res


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        left = a[:len(a) // 2]
        right = a[len(a) // 2:]
    return merge(merge_sort(left), merge_sort(right))


array_ = [round(random.uniform(0, 49), 3) for i in range(10)]
print(array_)
print(merge_sort(array_))
