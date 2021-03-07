"""
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.

Задача №1 из урока №3.
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

# Если начальные значения диапазонов равны (min_range = min_num)

import timeit
import cProfile


def multiple(max_range=99, min_num=2, max_num=9):
    count = {}
    for i in range(min_num, max_num + 1):
        count[i] = max_range // i
    return count


print(multiple())
# print(timeit.timeit('multiple()', globals=globals()))
# cProfile.run('multiple()')


"""
timeit
python -m timeit -n 100 -s "import les_4_task_1_2"
max_range=99
{2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
1.0086469
100 loops, best of 5: 9 nsec per loop

max_range=990
{2: 495, 3: 330, 4: 247, 5: 198, 6: 165, 7: 141, 8: 123, 9: 110}
1.0557788000000001
100 loops, best of 5: 9 nsec per loop

cProfile
max_range=99
{2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:17(multiple)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

max_range=990
{2: 495, 3: 330, 4: 247, 5: 198, 6: 165, 7: 141, 8: 123, 9: 110}
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:17(multiple)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Алгоритмическая сложность - О(1)
Самый быстрый и простой алгоритм,
но начальные значения диапазонов должны быть равны.
"""
