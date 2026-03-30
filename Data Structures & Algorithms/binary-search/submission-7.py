class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        i = n // 2
        r = n
        l = -1
        
        while i > l and i < r:
            num = nums[i]

            if num < target:
                l = i
                i = (i + r) // 2
            elif num > target:
                r = i
                i = (l + i) // 2
            else:
                return i
            
        return -1