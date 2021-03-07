"""
1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
"""

N = int(input('Введите кол-во друзей: '))

g = [[1 if i != j else 0 for i in range(N)] for j in range(N)]
print('Матрица смежности:')
print(*g, sep='\n')

handshakes = set()

for i, row in enumerate(g):
    for j, elem in enumerate(row):
        if elem:
            handshake = tuple(sorted((i, j)))
            handshakes.add(handshake)

count = len(handshakes)
print('Кол-во рукопожатий', count)

count2 = N * (N - 1) / 2
print('Кол-во рукопожатий по формуле', count2)
