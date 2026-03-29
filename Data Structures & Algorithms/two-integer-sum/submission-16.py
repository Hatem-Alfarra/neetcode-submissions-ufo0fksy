class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difDict = {}

        for i, val in enumerate(nums):
            difDict[i] = target - val

        for key, val in difDict.items():
            if val in set(nums):
                address = nums.index(val)
                if key != address:
                    first = min(key, address)
                    second = max(key, address)
                    return [first, second]

        