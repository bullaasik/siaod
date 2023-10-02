def tournament_sort(arr):
    n = len(arr)
    tree = [None] * (2 * n - 1)  # Инициализируем бинарное дерево
    
    # Заполняем листья бинарного дерева значениями из массива
    for i in range(n):
        tree[n - 1 + i] = (arr[i], i)
    
    # Строим бинарное дерево (турнир)
    for i in range(n - 2, -1, -1):
        tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])
    
    # Извлекаем элементы из турнира и строим отсортированный массив
    result = []
    while len(result) < n:
        min_val, min_index = tree[0]
        result.append(min_val)
        
        # Заменяем минимальное значение в дереве на бесконечность
        tree[n - 1 + min_index] = (float('inf'), min_index)
        
        # Продвигаем изменение значения вверх по дереву
        j = n - 1 + min_index
        while j > 0:
            j = (j - 1) // 2
            tree[j] = min(tree[2 * j + 1], tree[2 * j + 2])
    
    return result

# Пример использования
my_list = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_list = tournament_sort(my_list)
print(sorted_list)
