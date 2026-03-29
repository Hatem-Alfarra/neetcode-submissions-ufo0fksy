class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        for i in range(len(nums)):
            mul_result = 1
            for j in range(len(nums)):
                if i != j:
                    mul_result *= nums[j]
            solution.append(mul_result)
        return solution

