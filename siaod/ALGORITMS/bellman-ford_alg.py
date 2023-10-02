def bellman_ford(graph, src):
    num_vertices = len(graph)
    
    # Инициализация расстояний от источника до всех вершин как бесконечность
    distance = [float("inf")] * num_vertices
    distance[src] = 0

    # Проходим по всем вершинам V-1 раз (где V - количество вершин)
    for _ in range(num_vertices - 1):
        # Проходим по всем рёбрам и релаксируем их
        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = graph[u][v]
                if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                    # Если нашли более короткий путь, обновляем расстояние
                    distance[v] = distance[u] + weight

    # Проверяем наличие отрицательных циклов
    for u in range(num_vertices):
        for v in range(num_vertices):
            weight = graph[u][v]
            if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                print("Граф содержит отрицательный цикл")
                return None

    return distance

# Матрица смежности для графа
graph = [
    [0, 1, 4, 0, 0],
    [0, 0, 3, 2, 2],
    [0, 0, 0, 0, 0],
    [0, 1, 5, 0, 0],
    [0, 0, 0, 0, 0]
]

# Запускаем алгоритм, начиная с вершины 0
src_vertex = 0
result = bellman_ford(graph, src_vertex)

# Проверяем, есть ли результат (отрицательный цикл)
if result is not None:
    # Выводим кратчайшие расстояния от источника до всех вершин
    print("Вершина \t Расстояние от источника")
    for i, dist in enumerate(result):
        print(f"{i}\t\t{dist}")
