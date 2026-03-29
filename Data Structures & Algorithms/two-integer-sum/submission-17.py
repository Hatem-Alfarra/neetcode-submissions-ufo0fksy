class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difDict = {}

        for i, val in enumerate(nums):
            dif = target - val
            if val in difDict:
                return [int(difDict[val]) , i]
            else:
                difDict[dif] = str(i)