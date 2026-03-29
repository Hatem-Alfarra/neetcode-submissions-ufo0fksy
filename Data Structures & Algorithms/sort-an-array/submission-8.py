class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]) -> List[int]:
            """
            left and right should already be sorted
            """
            sortedList = []
            leftPointer, rightPointer = 0, 0

            while leftPointer < len(left) and rightPointer < len(right):
                if left[leftPointer] > right[rightPointer]:
                    sortedList.append(right[rightPointer])
                    rightPointer += 1
                else:
                    sortedList.append(left[leftPointer])
                    leftPointer += 1
            
            while leftPointer < len(left):
                sortedList.append(left[leftPointer])
                leftPointer += 1
            
            while rightPointer < len(right):
                sortedList.append(right[rightPointer])
                rightPointer += 1

            return sortedList
        
        def divideAndConquer(nums: List[int]):
            # breakdown list to individual elements
            # give elements to sort() and get out a sorted two element array
            # give sort() two element sorted array and get bigger sorted array and so on
            # final sort is the result
            if len(nums) == 1:
                return nums

            left, right = [], []
            rightPointer = int(len(nums)/2)

            left = divideAndConquer(nums[:rightPointer])
            right = divideAndConquer(nums[rightPointer:])
            return merge(left, right)
        
        return divideAndConquer(nums)

