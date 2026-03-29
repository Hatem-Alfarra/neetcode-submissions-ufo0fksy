class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        myList = []
        for num in nums:
            mySet.add(num)
            myList.append(num)
        if len(mySet) < len(myList):
            return True
        else:
            return False

        