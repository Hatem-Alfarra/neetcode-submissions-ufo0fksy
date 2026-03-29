class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numDays = len(temperatures)
        result = []


        for i in range(numDays):
            curTemp = temperatures[i]
            for j in range(i, numDays):
                if temperatures[j] > temperatures[i]:
                    dif = j - i
                    result.append(dif)
                    break
                elif j+1 == numDays:
                    result.append(0)
        
        return result

