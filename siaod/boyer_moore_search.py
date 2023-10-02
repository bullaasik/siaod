def boyer_moore_search(text, pattern):
    def build_bad_char_table(pattern):
        bad_char_table = {}
        pattern_length = len(pattern)
        for i in range(pattern_length - 1):
            bad_char_table[pattern[i]] = pattern_length - i - 1
        return bad_char_table

    def search_pattern(text, pattern):
        text_length = len(text)
        pattern_length = len(pattern)
        bad_char_table = build_bad_char_table(pattern)
        skip = 0

        while skip <= text_length - pattern_length:
            j = pattern_length - 1

            while j >= 0 and pattern[j] == text[skip + j]:
                j -= 1

            if j < 0:
                return skip

            skip += max(1, j - bad_char_table.get(text[skip + j], -1))

        return -1

    return search_pattern(text, pattern)

# Пример использования
text = "Это пример текста для поиска подстроки."
pattern = "поиска"
result = boyer_moore_search(text, pattern)

if result != -1:
    print(f"Подстрока найдена в позиции {result}")
else:
    print("Подстрока не найдена")
