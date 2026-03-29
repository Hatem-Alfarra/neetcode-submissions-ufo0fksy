class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones = 0, 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1

        for i in range(len(nums)):
            if zeros:
                nums[i] = 0
                zeros -= 1
            elif ones:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
        
            