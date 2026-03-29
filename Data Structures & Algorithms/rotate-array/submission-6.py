class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()

        k = k % len(nums)

        while k:
            num = nums.pop(0)
            nums.append(num)
            k -= 1
        
        nums.reverse()