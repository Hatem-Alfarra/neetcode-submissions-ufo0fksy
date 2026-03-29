class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org, cpy_set = nums, set(nums)
        return len(org) != len(cpy_set)
        