"""
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.

Задача №1 из урока №3.
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

import timeit
import cProfile


def multiple(min_range=2, max_range=990):
    count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(min_range, max_range + 1):

        if num % 2 == 0:
            count[2] += 1

        if num % 3 == 0:
            count[3] += 1

        if num % 4 == 0:
            count[4] += 1

        if num % 5 == 0:
            count[5] += 1

        if num % 6 == 0:
            count[6] += 1

        if num % 7 == 0:
            count[7] += 1

        if num % 8 == 0:
            count[8] += 1

        if num % 9 == 0:
            count[9] += 1

    return count


print(multiple())
# print(timeit.timeit('multiple()', globals=globals()))
# cProfile.run('multiple()')


"""
timeit
python -m timeit -n 100 -s "import les_4_task_1_2"
max_range=99
{2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
55.223070199999995
100 loops, best of 5: 9 nsec per loop

max_range=990
{2: 495, 3: 330, 4: 247, 5: 198, 6: 165, 7: 141, 8: 123, 9: 110}
559.3636013
100 loops, best of 5: 9 nsec per loop

cProfile
max_range=99
{2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:15(multiple)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

max_range=990
{2: 495, 3: 330, 4: 247, 5: 198, 6: 165, 7: 141, 8: 123, 9: 110}
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les_4_task_1_3.py:15(multiple)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Алгоритмическая сложность - О(n)
"""
