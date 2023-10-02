def compute_prefix(pattern):
    """
    Функция вычисления таблицы префиксов для паттерна.
    
    :param pattern: Строка-паттерн
    :return: Таблица префиксов
    """
    prefix_table = [0] * len(pattern)
    length = 0  # Длина текущего префикса

    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = prefix_table[length - 1]
        
        if pattern[i] == pattern[length]:
            length += 1
        
        prefix_table[i] = length

    return prefix_table

def kmp_search(text, pattern):
    """
    Функция поиска паттерна в тексте с использованием алгоритма KMP.
    
    :param text: Текст, в котором ищется паттерн
    :param pattern: Строка-паттерн
    :return: Список индексов, где найден паттерн (пустой список, если не найден)
    """
    prefix_table = compute_prefix(pattern)
    indices = []  # Список для хранения индексов, где найден паттерн
    j = 0  # Индекс для паттерна

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == len(pattern):
            # Найден паттерн
            indices.append(i - j + 1)
            j = prefix_table[j - 1]

    return indices

# Пример использования
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp_search(text, pattern)
print("Индексы, где найден паттерн:", result)
