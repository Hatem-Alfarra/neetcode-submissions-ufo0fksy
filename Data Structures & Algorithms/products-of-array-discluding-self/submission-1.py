class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        mul_result = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                mul_result *= nums[i]
            else:
                zeros += 1
        for j in range(len(nums)):
            if zeros == 0:
                solution.append(int(mul_result/nums[j]))
            else:
                if zeros == 1:
                    if nums[j] == 0:
                        solution.append(mul_result)
                    else:
                        solution.append(0)
                else:
                    solution.append(0)

        return solution

