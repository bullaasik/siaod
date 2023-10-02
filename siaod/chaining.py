class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                # Если ключ уже существует, обновляем значение
                item[1] = value
                return
        # Если ключ не найден, добавляем новую пару ключ-значение
        self.table[index].append([key, value])

    def get(self, key, default=None):
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
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
