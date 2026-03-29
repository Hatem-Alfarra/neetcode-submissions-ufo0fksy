class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum_ = lastop = lastlastop = lastlastlastop = 0
        
        for operation in operations:
            if operation == "+":
                temp = lastop + lastlastop
                sum_ += temp
                lastlastlastop = lastlastop
                lastlastop = lastop
                lastop = temp
            elif operation == "C":
                sum_ -= lastop
                lastop = lastlastop
                lastlastop = lastlastlastop
                lastlastlastop = 0
            elif operation == "D":
                sum_ += lastop + lastop
                lastlastlastop = lastlastop
                lastlastop = lastop
                lastop = lastop + lastop
            else:
                lastlastlastop = lastlastop
                lastlastop = lastop
                lastop = int(operation)
                sum_ += lastop            
            
        return sum_