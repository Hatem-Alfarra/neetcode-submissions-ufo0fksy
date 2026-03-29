class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i = j = 0 
        res = []
        length = len(nums)
        for i in range(length):
            prod = 1
            for j in range(length):
                if i == j:
                    continue
                prod *= nums[j]
            res.append(prod)
        
        return res