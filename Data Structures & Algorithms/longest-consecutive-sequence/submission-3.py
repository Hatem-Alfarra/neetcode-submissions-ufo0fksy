class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        count = 0
        counts = []
        exp = "Not_determined"
        for num in nums:
            if num == exp:
                count += 1
            else:
                count = 1
            counts.append(count)
            exp = num + 1
        if counts:
            return max(counts)
        else:
            return 0