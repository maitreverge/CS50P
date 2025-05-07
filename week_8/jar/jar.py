class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        result = ""
        for _ in range(self._size):
            result += "🍪"
        return result

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Max capacity excedeed")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError(f"You can't withdraw {n} coockies. Max Size = {self._size}")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
