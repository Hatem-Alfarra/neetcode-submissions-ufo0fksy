class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodForwards = prodBackwards = 1
        res = []
        length = len(nums)

        for i in range(length):
            res.append(prodForwards)
            prodForwards *= nums[i]
        for j in range(length-1, -1, -1):
            res[j] *= prodBackwards
            prodBackwards *= nums[j] 

        return res
