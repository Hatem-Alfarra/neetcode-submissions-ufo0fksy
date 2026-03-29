class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.data = [False]*(self.size+1)
        
    def add(self, key: int) -> None:
        while key > self.size:
            self.size = self.size * 2
            self.data = self.data + [False]*((self.size//2)+1)
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


        
