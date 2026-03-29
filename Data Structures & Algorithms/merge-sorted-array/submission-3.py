class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """   # [1,2,2,3,5,6]
        indx = i = m + n - 1   # indx = i = 3 + 3 - 1 = 5
        j = n - 1 # j = 3 - 1 = 2

        while indx >= 0 and j >= 0:          # while 5 >= 0 and 2 >= 0:
            if nums1[indx] == 0:             # if 0 == 0: indx-- -> indx = 2
                indx -= 1
            elif nums1[indx] > nums2[j]:     # if 3 > 6 (false): | if 3 > 5 (false) | if 3 > 2 true | if 2 > 2: false
                nums1[i] = nums1[indx]       # nums1[3] = 3 | 
                i -= 1                       # i = 2
                indx -= 1                    # indx = 1
            elif nums1[indx] <= nums2[j]:    # if 3 <= 6 (true): | if 3 <= 5 true | if 2 <= 2 true
                nums1[i] = nums2[j]          # nums1[5] = 6   | nums[4] = 5 | nums[2] = 2
                i -= 1                       # i = 5-1= 4  | i = 3 | i = 1
                j -= 1                       # j = 2-1 = 1 | j = 0 | j = -1
        
        if j > -1:
            nums1[:i+1] = nums2[:j+1]            # [1, 2] = []

