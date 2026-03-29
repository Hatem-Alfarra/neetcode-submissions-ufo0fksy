class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monotonicStack = []

        for i, dayT in enumerate(temperatures):
            while monotonicStack and dayT > temperatures[monotonicStack[-1]]:
                firstIndx = monotonicStack.pop()
                res[firstIndx] = i - firstIndx
            monotonicStack.append(i)
        
        return res
                
            