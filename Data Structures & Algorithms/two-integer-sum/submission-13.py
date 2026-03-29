class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        n = 0
        for i in nums:
            difference = target - i
            if difference in my_dict:
                return [my_dict[difference], n]
            else:
                my_dict[i] = n
                n += 1 
                
