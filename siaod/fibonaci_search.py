def fibonacci_search(arr, x):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_current = fib_m_minus_1 + fib_m_minus_2

    # Находим ближайшее число Фибоначчи, которое больше или равно длине массива
    while fib_current < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_current
        fib_current = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib_current > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)

        if arr[i] < x:
            fib_current = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_current - fib_m_minus_1
            offset = i

        elif arr[i] > x:
            fib_current = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_current - fib_m_minus_1

        else:
            return i  # Элемент найден

    if fib_m_minus_1 and arr[offset + 1] == x:
        return offset + 1  # Элемент найден

    return -1  # Элемент не найден

# Пример использования:
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85

result = fibonacci_search(arr, x)
if result != -1:
    print(f"Элемент {x} найден по индексу {result}.")
else:
    print(f"Элемент {x} не найден в массиве.")
