class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = ""

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if len(self.min_val) > 0:
        #     if int(self.min_val) < val:
        #         self.min_val = val
        # else:
        #     self.min_val = val
        # self.min_val = min(self.stack)

    def pop(self) -> None:
        self.stack.pop()

        

    def top(self) -> int:
        if len(self.stack) > 0:
            top = self.stack[-1]
            return top
        return None
        

    def getMin(self) -> int:
        return min(self.stack)


        
