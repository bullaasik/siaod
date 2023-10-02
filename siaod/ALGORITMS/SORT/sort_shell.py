def shell_sort(arr):
    n = len(arr)
    gap = len(arr) // 2  # Начальный размер шага (разделяем массив на две половины)
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Сдвигаем элементы, находящиеся на расстоянии gap, если они больше temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Вставляем temp в правильную позицию
            arr[j] = temp
        
        # Уменьшаем размер шага вдвое
        gap //= 2

# Пример использования
my_list = input('введите числа').split()
shell_sort(my_list)
print(my_list)
