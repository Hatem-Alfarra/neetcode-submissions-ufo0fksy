class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortedArray = []
        if not nums:
            return sortedArray
        
        for numSorting in nums:
            indexSorted = 0
            for numSorted in sortedArray:
                if numSorted > numSorting:
                    sortedArray.insert(indexSorted, numSorting)
                    break
                indexSorted += 1
            if indexSorted == len(sortedArray):
                sortedArray.append(numSorting)
                

        for k in range(len(nums)):
            nums[k] = sortedArray[k]

            