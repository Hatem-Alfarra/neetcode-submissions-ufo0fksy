class MyHashMap:

    def __init__(self):
        self.size = 1000000
        self.data = [-1]*(self.size+1)
        
    def put(self, key: int, value: int) -> None:
        self.extend(key)
        self.data[key] = value
        
    def get(self, key: int) -> int:
        if key > (self.size - 1):
            return -1
        return self.data[key]

    def remove(self, key: int) -> None:
        if key > (self.size - 1):
            return
        self.data[key] = -1
    
    def extend(self, key: int) -> None:
        while key > (self.size - 1):
            self.data += [-1]*self.size
            self.size *= 2


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)