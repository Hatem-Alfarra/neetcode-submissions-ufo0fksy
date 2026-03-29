class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        prevNum = None

        for i, num in enumerate(nums):
            if num == prevNum:
                continue
            prevNum = num
            subtarget = 0 - num
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                twoSum = nums[l] + nums[r]

                if twoSum > subtarget:
                    r -= 1
                elif twoSum < subtarget:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res