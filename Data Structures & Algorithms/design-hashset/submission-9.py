class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]
        
    def add(self, key: int) -> None:
        hashed = key % self.size
        if key not in self.data[hashed]:
            self.data[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = key % self.size
        if key in self.data[hashed]:
            self.data[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = key % self.size
        return key in self.data[hashed]
