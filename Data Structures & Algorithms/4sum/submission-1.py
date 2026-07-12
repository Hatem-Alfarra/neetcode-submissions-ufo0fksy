class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)

        for i in range(length-3):
            for j in range(i+1, length-2):
                for k in range(j+1, length-1):
                    for l in range(k+1, length):
                        curSum = nums[i] + nums[j] + nums[k] + nums[l]
                        if curSum == target:
                            if [nums[i], nums[j], nums[k], nums[l]] not in ans:
                                ans.append( [nums[i], nums[j], nums[k], nums[l]] )

        return ans

