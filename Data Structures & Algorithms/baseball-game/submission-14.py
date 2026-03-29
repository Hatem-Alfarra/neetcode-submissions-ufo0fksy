class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        collection = []
        for operation in operations:
            if operation == "+":
                val = int(collection[-1]) + int(collection[-2])
                res += val
                collection.append(val)
            elif operation == "C":
                res -= collection.pop()
            elif operation == "D":
                val = int(collection[-1])*2
                res += val
                collection.append(val)
            else:
                val = int(operation)
                res += val
                collection.append(int(operation))
            
        return res