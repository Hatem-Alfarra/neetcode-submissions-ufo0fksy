class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortedArray = [] # ex. nums = [], [1], [1, 2], [2, 1]
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
                
        return sortedArray