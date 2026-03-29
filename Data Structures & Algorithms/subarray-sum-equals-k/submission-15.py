class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        res = curSum = 0 

        for num in nums:
            curSum += num
            dif = curSum - k

            res += prefixSums.get(dif, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res