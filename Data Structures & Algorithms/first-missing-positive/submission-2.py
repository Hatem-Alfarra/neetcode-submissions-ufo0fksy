class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallestInt = 1
        bins = max(100, max(nums))
        hashSet = [[] for _ in range(bins)]

        for num in nums:
            if num == smallestInt:
                smallestInt += 1
            
            if num > smallestInt:
                hashed = num % bins
                if num not in hashSet[hashed]:
                    hashSet[hashed].append(num)
            
            hashedSmallestInt = smallestInt % bins
            while smallestInt in hashSet[hashedSmallestInt]:
                smallestInt += 1
                hashedSmallestInt = smallestInt % bins
        
        return smallestInt
