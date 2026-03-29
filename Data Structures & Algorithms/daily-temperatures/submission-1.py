class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unsolved = {}
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # logic for checking if current values solves previous unsolved values
            unsolvedCopy = dict(unsolved)
            for j, prevTemp in unsolvedCopy.items():
                if temp > prevTemp:
                    diff = i - j
                    result[j] = diff
                    unsolved.pop(j)
                    

            # add current value
            unsolved[i] = temp

        return result