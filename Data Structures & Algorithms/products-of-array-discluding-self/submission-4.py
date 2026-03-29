class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodForwards = prodBackwards = 1
        res = []
        length = len(nums)

        # 1, 2, 4, 6
        # 1, 1*1, 1*1*2, 1*1*2*4
        # 1 * 1*1*6*4*2, 1*1 *1*6*4, 1*1*2 *1*6, 1*1*2*4 *1
        # 48, 24, 12, 8

        # 2, 2, 4, 6
        # 1, 1*2, 1*2*2, 1*2*2*4
        # 1 *6*4*2, 1*2 *6*4, 1*2*2 *6, 1*2*2*4
        # 48, 24, 12, 8

        for i in range(length):
            res.append(prodForwards)
            prodForwards *= nums[i]
        for j in range(length-1, -1, -1):
            res[j] *= prodBackwards
            prodBackwards *= nums[j] 

        return res
