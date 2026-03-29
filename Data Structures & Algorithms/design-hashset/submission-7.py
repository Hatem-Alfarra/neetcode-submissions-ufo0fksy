class MyHashSet:

    def __init__(self):
        self.size = 100
        self.data = [False]*(self.size+1)
        
    def add(self, key: int) -> None:
        self.extend(key)
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.extend(key)
        self.data[key] = False

    def contains(self, key: int) -> bool:
        self.extend(key)
        return self.data[key]
    
    def extend(self, key: int) -> None:
        while key > self.size:
            self.size *= 2
            self.data += [False]*len(self.data)

        
