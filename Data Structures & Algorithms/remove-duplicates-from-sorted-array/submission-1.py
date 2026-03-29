class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        og_len = len(nums)
        left = right = 0

        while right < og_len:
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        
        return left + 1

                

