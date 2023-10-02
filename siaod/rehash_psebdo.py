import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        while self.table[index] is not None:
            # Генерируем случайный индекс для рехэширования
            index = (index + random.randint(1, self.size - 1)) % self.size
        self.table[index] = (key, value)

    def get(self, key, default=None):
        index = self.hash(key)
        while self.table[index] is not None:
            stored_key, value = self.table[index]
            if stored_key == key:
                return value
            # Генерируем случайный индекс для рехэширования
            index = (index + random.randint(1, self.size - 1)) % self.size
        return default

    def __str__(self):
        return str(self.table)

# Пример использования
if __name__ == "__main__":
    hashtable = HashTable(10)
    hashtable.insert("apple", 10)
    hashtable.insert("banana", 5)
    hashtable.insert("cherry", 20)

    print(hashtable.get("apple"))  # Выведет 10
    print(hashtable.get("banana"))  # Выведет 5
    print(hashtable.get("cherry"))  # Выведет 20
    print(hashtable.get("grape"))  # Выведет None (если ключ отсутствует)
