# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

M = int(input('Число столбцов: '))
N = int(input('Число строк: '))
matrix = []
for i in range(N):
    row = []
    for j in range(M):
        n = random.randint(0, 100)
        row.append(n)
        print('%4d' % n, end='')
    matrix.append(row)
    print()

max_ = 0
for j in range(M):
    min_ = matrix[0][j]
    for i in range(N):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]
    if min_ > max_:
        max_ = min_
print("Максимальный среди минимальных:", max_)
