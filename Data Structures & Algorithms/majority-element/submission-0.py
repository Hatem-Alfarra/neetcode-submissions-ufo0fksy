class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqDict = {}

        for num in nums:
            if num not in freqDict:
                freqDict[num] = 1;
            else:
                freqDict[num] += 1
        
        maxVal = nums[0]
        maxfreq = 0

        for number, freq in freqDict.items():
            if freq > maxfreq:
                maxfreq = freq
                maxVal = number
        
        return maxVal
