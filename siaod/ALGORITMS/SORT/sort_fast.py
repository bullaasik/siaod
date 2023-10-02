def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Если массив пустой или содержит только один элемент, он уже отсортирован

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (можно выбрать и другой способ)

    # Разбиваем массив на элементы, меньше опорного, равные опорному и больше опорного
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Рекурсивно сортируем подмассивы меньших и больших элементов
    return quick_sort(less) + equal + quick_sort(greater)

# Пример использования
my_list = input().split()
sorted_list = quick_sort(my_list)
print(sorted_list)