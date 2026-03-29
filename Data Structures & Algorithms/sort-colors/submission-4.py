class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones, twos = 0,0

        for num in nums:
            if num == 1:
                ones += 1
            elif num == 2:
                twos += 1
        
        
        numsSorted = [0] * (len(nums)-(ones+twos)) + [1] * ones + [2] * twos

        for i in range(len(nums)):
            nums[i] = numsSorted[i]
        
            