class Node:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 1000 # number of bins
        self.data = [Node() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hashed = self.hash(key)
        currentBinHead = self.data[hashed]
        curNode = currentBinHead

        while curNode.next:
            if curNode.next.key == key:
                curNode.next.value = value
                return
            curNode = curNode.next
            
        curNode.next = Node(key, value)

        
    def get(self, key: int) -> int:
        hashed = self.hash(key)
        currentBinHead = self.data[hashed]
        curNode = currentBinHead
        
        while curNode.next:
            if curNode.next.key == key:
                return curNode.next.value
            curNode = curNode.next
        
        return -1


    def remove(self, key: int) -> None:
        hashed = self.hash(key)
        currentBinHead = self.data[hashed]
        curNode = currentBinHead

        while curNode.next:
            if curNode.next.key == key:
                curNode.next = curNode.next.next
                return
            curNode = curNode.next

    
    def hash(self, key: int) -> int:
        return key % self.size

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)