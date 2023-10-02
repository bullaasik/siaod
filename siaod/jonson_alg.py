import math
import heapq

def bellman_ford(graph, source):
    num_vertices = len(graph)
    distance = [math.inf] * num_vertices
    distance[source] = 0
    
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in enumerate(graph[u]):
                if weight is not None and distance[u] != math.inf and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    
    return distance

def johnson(graph):
    num_vertices = len(graph)
    
    # Добавление фиктивной вершины и рёбер нулевого веса к каждой вершине
    augmented_graph = [[0] * (num_vertices + 1) for _ in range(num_vertices + 1)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            augmented_graph[i][j] = graph[i][j]
    
    # Вычисление потенциалов с помощью алгоритма Беллмана-Форда
    potentials = bellman_ford(augmented_graph, num_vertices)
    
    # Модификация весов рёбер
    for u in range(num_vertices):
        for v in range(num_vertices):
            if graph[u][v] is not None:
                augmented_graph[u][v] += potentials[u] - potentials[v]
    
    # Вычисление кратчайших путей с использованием алгоритма Дейкстры
    shortest_paths = []
    for u in range(num_vertices):
        distances = [math.inf] * num_vertices
        distances[u] = 0
        heap = [(0, u)]
        
        while heap:
            dist_u, u = heapq.heappop(heap)
            if dist_u > distances[u]:
                continue
            for v, weight in enumerate(augmented_graph[u]):
                if weight is not None and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(heap, (distances[v], v))
        
        # Коррекция путей с учетом потенциалов
        corrected_paths = []
        for v in range(num_vertices):
            if distances[v] != math.inf:
                path = [v]
                while v != u:
                    for w, weight in enumerate(augmented_graph[v]):
                        if weight is not None and distances[v] == distances[u] + weight:
                            path.append(w)
                            v = w
                            break
                path.reverse()
                corrected_paths.append((u, v, path))
        
        shortest_paths.append(corrected_paths)
    
    return shortest_paths

# Пример использования алгоритма
if __name__ == "__main__":
    # Матрица смежности для графа (None означает отсутствие ребра)
    graph = [
        [0, 2, None, 3],
        [None, 0, 4, None],
        [None, None, 0, 1],
        [None, None, None, 0]
    ]

    shortest_paths = johnson(graph)
    
    # Вывод кратчайших путей
    for u in range(len(shortest_paths)):
        for v, path in enumerate(shortest_paths[u]):
            print(f"Кратчайший путь от вершины {u} до вершины {v}: {path}")
