class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # go through num1 until index m-1. if you encounter value greater than num2 value
        # insert the new value after shifting the array forward
        i = 0
        j = 0
        while i < m:
            if j < n and nums1[i] > nums2[j]:
                # insert
                temp = nums1[i]
                nums1[i] = nums2[j]

                # shift
                for k in range(i+1, m+1):
                    temp2 = nums1[k]
                    nums1[k] = temp
                    temp = temp2
                
                m += 1
                i += 1
                j += 1
            else:
                i += 1
        
        nums1[m:] = nums2[j:]
            

                
