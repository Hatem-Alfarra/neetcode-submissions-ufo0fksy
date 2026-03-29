class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = set()

        for m in range(1, n-1):
            l = m - 1
            r = m + 1

            while l >= 0:
                s = nums[l] + nums[m] + nums[r]
                while s < 0:
                    if r + 1 < n:
                        r += 1
                    else:
                        break
                    s = nums[l] + nums[m] + nums[r]
                if s == 0:
                    if (nums[l], nums[m], nums[r]) not in res:
                        res.add((nums[l], nums[m], nums[r]))
                l -= 1
        

        return [list(t) for t in res]


