class Solution:
    def calPoints(self, operations: List[str]) -> int:
        collection = []
        for operation in operations:
            if operation == "+":
                collection.append(int(collection[-1]) + int(collection[-2]))
            elif operation == "C":
                collection.pop()
            elif operation == "D":
                collection.append(int(collection[-1])*2)
            else:
                collection.append(int(operation))
            
        return sum(collection)