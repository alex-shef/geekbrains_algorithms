"""
Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parents = [-1] * length

    start_ = start                   # запоминаем начальную вершину
    parents[start_] = start_
    way = {}                         # словарь "вершина : список вершин до неё"
    top_list = []                    # список вершин

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parents[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    # для решения задачи работаем со списком "parents"
    for i, parent in enumerate(parents):
        if i == start_:
            way[i] = [parent]               # добавляем начальную вершину
        elif parent == -1:
            way[i] = 'нет пути'
        else:
            k = i                           # создаём переменную-индекс
            top_list.append(k)              # для итерации по "parents"
            while start_ not in top_list:
                top_list.append(parents[k])
                k = parents[k]
            top_list.reverse()
            way[i] = top_list
            top_list = []

    return cost, way


s = int(input('От какой вершины идти: '))
cost_, way_ = dijkstra(g, s)

print('Кратчайшие пути:', cost_)
print('Список вершин:')
for key, value in way_.items():
    print(key, ':', value)
