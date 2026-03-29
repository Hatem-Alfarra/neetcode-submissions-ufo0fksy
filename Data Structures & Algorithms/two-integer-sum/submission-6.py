class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_dict = {}
        for n in range(len(nums)):
            num = nums[n]
            dif = target - num
            if dif in visited_dict:
                return [visited_dict[dif], n]
            else:
                visited_dict[num] = n 

        return []
                
