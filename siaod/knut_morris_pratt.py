def build_failure_table(pattern):
    # Создаем таблицу сдвигов для префикс-функции
    failure_table = [0] * len(pattern)
    j = 0  # Индекс для обхода pattern

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        failure_table[i] = j

    return failure_table

def kmp_search(text, pattern):
    failure_table = build_failure_table(pattern)
    j = 0  # Индекс для обхода pattern

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = failure_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            # Найдено совпадение, возвращаем индекс начала подстроки в тексте
            return i - j + 1

    # Подстрока не найдена
    return -1

# Пример использования
if __name__ == "__main__":
    text = "ABCABCABDABABCABCDABCDABCABDE"
    pattern = "ABCDABD"
    result = kmp_search(text, pattern)

    if result != -1:
        print(f"Подстрока найдена в позиции {result}")
    else:
        print("Подстрока не найдена")
