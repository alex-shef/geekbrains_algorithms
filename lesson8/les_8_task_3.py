"""
Написать программу, которая обходит не взвешенный ориентированный граф
без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
"""


def graph(n):
    i = 0
    g = [[0] * (n - 1) for _ in range(n)]
    while i < n:
        g[i] = [_ for _ in range(n)]
        g[i].pop(i)
        set(g[i])
        i += 1
    return g


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return print(visited)


n_ = int(input("Введите кол-во вершин:"))
graph_ = graph(n_)
print(*graph_, sep='\n')
print("*" * 10)
dfs(graph_, 0)
