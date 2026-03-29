class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict for target - vals. 
        difDict = {}
        # For val in nums: dif in dict
        for i, val in enumerate(nums):
            difDict[i] = target - val
        # For val in nums: if val in dict (not same address though) return those two
        for key, val in difDict.items():
            if val in set(nums):
                address = nums.index(val)
                if key != address:
                    first = min(key, address)
                    second = max(key, address)
                    return [first, second]

        