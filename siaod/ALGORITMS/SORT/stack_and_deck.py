# Создаем пустой стек
stack = []

# Добавляем элементы в стек
stack.append(1)
stack.append(2)
stack.append(3)

# Стек сейчас выглядит как [1, 2, 3]

# Извлекаем элементы из стека
top_element = stack.pop()  # Удалит и вернет 3
next_element = stack.pop()  # Удалит и вернет 2

# Теперь стек содержит только [1]


from collections import deque

# Создаем пустой дек
deque = deque()

# Добавляем элементы в начало и конец дека
deque.append(1)       # [1]
deque.appendleft(2)   # [2, 1]
deque.append(3)       # [2, 1, 3]

# Извлекаем элементы с обоих концов дека
first_element = deque.popleft()  # Удалит и вернет 2
last_element = deque.pop()       # Удалит и вернет 3

# Теперь дек содержит только [1]
