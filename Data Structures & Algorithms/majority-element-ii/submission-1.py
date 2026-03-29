class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {} 
        res = set()
        n = len(nums)

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
            if freq[num] > n/3:
                res.add(num)
        
        
        return list(res)