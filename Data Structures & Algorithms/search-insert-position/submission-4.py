class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        mid = r // 2
        l = 0

        while l < r-1:
            cur = nums[mid]

            if cur > target:
                mid = (l + mid) // 2
                r = mid + 1                
            elif cur < target:
                mid = (r + mid + 1) // 2
                l = mid - 1
            else:
                return mid
        
        if nums[mid] >= target:
            return mid
        else:
            return mid+1