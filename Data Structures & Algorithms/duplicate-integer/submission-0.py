class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mylist = []
        for num in nums:
            if num in mylist:
                return True
            else:
                mylist.append(num)
        return False

        