# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

M = 5
N = 4
matrix = []
print('По одному через Enter:')
for i in range(1, N+1):
    row = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M - 1):
        n = int(input())
        s += n
        row.append(n)
    row.append(s)
    matrix.append(row)

for row in matrix:
    print(row)
