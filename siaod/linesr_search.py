def linear_search_substring(text, substring):
    text_length = len(text)
    substring_length = len(substring)

    for i in range(text_length - substring_length + 1):
        if text[i:i + substring_length] == substring:
            return i

    return -1

# Пример использования
text = "Это пример текста для поиска подстроки."
substring = "поиска"
result = linear_search_substring(text, substring)

if result != -1:
    print(f"Подстрока найдена в позиции {result}")
else:
    print("Подстрока не найдена")
