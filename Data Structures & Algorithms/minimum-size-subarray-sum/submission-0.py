class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        solutions_lengths = set()
        length = len(nums)
        l, r = 0, length-1
        
        while l <= r:    
            m = l
            cur_sum = 0
            while m <= r:
                cur_sum += nums[m]
                if cur_sum >= target:
                    solutions_lengths.add(m-l+1)
                    break
                else:
                    m += 1
            l += 1
        
        if solutions_lengths:
            return min(solutions_lengths)
        else:
            return 0