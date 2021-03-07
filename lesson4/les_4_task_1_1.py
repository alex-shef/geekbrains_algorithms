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


def multiple(min_range=2, max_range=99, min_num=2, max_num=9):
    count = {}
    for i in range(min_num, max_num + 1):
        count[i] = 0
        for j in range(min_range, max_range + 1):
            if j % i == 0:
                count[i] += 1
    return count


print(multiple())
# print(timeit.timeit('multiple()', globals=globals()))
# cProfile.run('multiple()')


"""
timeit
python -m timeit -n 100 -s "import les_4_task_1_1"
max_range=99
{2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
66.0455957
100 loops, best of 5: 9 nsec per loop

max_range=990
{2: 495, 3: 330, 4: 247, 5: 198, 6: 165, 7: 141, 8: 123, 9: 110}
699.5702057000001
100 loops, best of 5: 21 nsec per loop

cProfile
max_range=99
{2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:36(multiple)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

max_range=990
{2: 495, 3: 330, 4: 247, 5: 198, 6: 165, 7: 141, 8: 123, 9: 110}
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les_4_task_1_1.py:15(multiple)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Алгоритмическая сложность - О(n)
Самый оптимальный алгоритм из трёх,
т.к. можно использовать для любых входных данных.
"""
