class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for order_i in range(len(nums)):
            for order_j_minus_i in range(1, len(nums)-order_i):
                if target == (nums[order_i + order_j_minus_i] + nums[order_i]):
                    return [order_i, order_i + order_j_minus_i]