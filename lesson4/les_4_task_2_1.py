"""
Решето Эратосфена.
Функция самостоятельно расширяет массив при необходимости.
Не придумал только, как использовать этот метод сразу в расширенной части(без
 повторного прохода).
"""
import timeit
import cProfile


def eratosthenes(n):  # n - номер простого числа, которое нужно получить

    size = n * 3  # начальный размер массива
    sieve = [i for i in range(size)]
    sieve[1] = 0
    result = []  # будущий массив простых чисел

    while len(result) < n:
        for i in range(2, size):
            if sieve[i] != 0:
                j = i * 2
                while j < size:
                    sieve[j] = 0
                    j += i
                if sieve[i] not in result:  # условие нужно при расширении массива
                    result.append(sieve[i])
                # if len(result) == n:
                #     return result[n - 1]

        for i in range(size, size * 2):  # расширение массива при необходимости
            sieve.append(i)
        size = size * 2

    return result[n - 1]


print(eratosthenes(10))
print(eratosthenes(20))
print(eratosthenes(30))
print(eratosthenes(50))
print(eratosthenes(100))

# print(timeit.timeit('eratosthenes(10)', globals=globals()))
# print(timeit.timeit('eratosthenes(20)', globals=globals()))
# print(timeit.timeit('eratosthenes(30)', globals=globals()))
# print(timeit.timeit('eratosthenes(50)', globals=globals()))
# print(timeit.timeit('eratosthenes(100)', globals=globals()))

# print(eratosthenes(1000))
# print(eratosthenes(10000))

# cProfile.run('eratosthenes(10)')
# cProfile.run('eratosthenes(20)')
# cProfile.run('eratosthenes(30)')
# cProfile.run('eratosthenes(50)')
# cProfile.run('eratosthenes(100)')
# cProfile.run('eratosthenes(1000)')
# cProfile.run('eratosthenes(10000)')


"""
timeit
python -m timeit -n 100 -s "import les_4_task_2_1"
n=10
answer=29
9.7916045

n=20
answer=71
49.7545581

n=30
answer=113
78.8340571

n=50
answer=229
146.5692518

n=100
answer=541
385.890911

n=1000
answer=7919

n=10000
answer=104729

100 loops, best of 5: 9 nsec per loop
"""


"""
cProfile

cProfile.run('eratosthenes(10)')

        25 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:11(eratosthenes)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:14(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('eratosthenes(20)')

         122 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:11(eratosthenes)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:14(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       37    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('eratosthenes(30)')

         179 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:11(eratosthenes)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:14(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       54    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      120    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('eratosthenes(50)')

         290 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:11(eratosthenes)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:14(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       85    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('eratosthenes(100)')

         567 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:11(eratosthenes)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:14(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      162    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      400    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('eratosthenes(1000)')

         12218 function calls in 0.021 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.021    0.021 <string>:1(<module>)
        1    0.019    0.019    0.021    0.021 les_4_task_2_1.py:11(eratosthenes)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:14(<listcomp>)
        1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
     2213    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('eratosthenes(10000)')

         119307 function calls in 1.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.019    1.019 <string>:1(<module>)
        1    1.004    1.004    1.019    1.019 les_4_task_2_1.py:11(eratosthenes)
        1    0.001    0.001    0.001    0.001 les_4_task_2_1.py:14(<listcomp>)
        1    0.000    0.000    1.019    1.019 {built-in method builtins.exec}
    19302    0.003    0.000    0.003    0.000 {built-in method builtins.len}
   100000    0.011    0.000    0.011    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Самый быстрый алгоритм. Сложность O(n*log(log(n))).
"""
