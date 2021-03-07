import timeit
import cProfile


def prime(n):  # n - номер простого числа, которое нужно получить

    start = 3
    end = n * 3  # предел диапазона
    result = [2]  # массив простых чисел

    while True:
        for i in range(start, end, 2):
            for j in range(3, i, 2):
                if (i % j) == 0:
                    break
            else:
                if i not in result:  # условие нужно при расширении диапазона
                    result.append(i)
            if len(result) == n:
                return result[n - 1]

        start = result[-1]  # расширение диапазона при необходимости
        end = end * 3


print(prime(10))
print(prime(20))
print(prime(30))
print(prime(50))
print(prime(100))

# print(timeit.timeit('prime(10)', globals=globals()))
# print(timeit.timeit('prime(20)', globals=globals()))
# print(timeit.timeit('prime(30)', globals=globals()))
# print(timeit.timeit('prime(50)', globals=globals()))
# print(timeit.timeit('prime(100)', globals=globals()))

print(prime(1000))
print(prime(10000))

# cProfile.run('prime(10)')
# cProfile.run('prime(20)')
# cProfile.run('prime(30)')
# cProfile.run('prime(50)')
# cProfile.run('prime(100)')
# cProfile.run('prime(1000)')
# cProfile.run('prime(10000)')

"""
timeit
python -m timeit -n 100 -s "import les_4_task_2_2"
n=10
answer=29
10.071355700000002

n=20
answer=71
37.893577300000004

n=30
answer=113
77.4159491

n=50
answer=229
219.32699480000002

n=100
answer=541
958.8980862000001

n=1000
answer=7919

n=10000
answer=104729

100 loops, best of 5: 9 nsec per loop
"""

"""
cProfile

cProfile.run('prime(10)')

         27 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_2.py:5(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       14    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(20)')

         59 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_2.py:5(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       19    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(30)')

         90 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_2.py:5(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       57    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       29    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(50)')

         168 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2_2.py:5(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      115    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       49    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(100)')

         377 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les_4_task_2_2.py:5(prime)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      274    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(1000)')

         4963 function calls in 0.154 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.154    0.154 <string>:1(<module>)
        1    0.153    0.153    0.154    0.154 les_4_task_2_2.py:5(prime)
        1    0.000    0.000    0.154    0.154 {built-in method builtins.exec}
     3960    0.001    0.000    0.001    0.000 {built-in method builtins.len}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(10000)')

         62379 function calls in 34.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   34.019   34.019 <string>:1(<module>)
        1   34.009   34.009   34.019   34.019 les_4_task_2_2.py:5(prime)
        1    0.000    0.000   34.019   34.019 {built-in method builtins.exec}
    52376    0.007    0.000    0.007    0.000 {built-in method builtins.len}
     9999    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
