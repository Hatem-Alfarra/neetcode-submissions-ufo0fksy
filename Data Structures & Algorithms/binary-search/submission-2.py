class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        i = n // 2
        r = n
        l = -1

        # num = nums[i]
        # if num == target:
        #     return i
        
        while i > l and i < r:
            num = nums[i]

            if num == target:
                return i
            elif num > target:
                r = i
                i = i // 2
            elif num < target:
                l = i
                i = (i + r) // 2
        return -1