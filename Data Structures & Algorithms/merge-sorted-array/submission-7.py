class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        indx = i = m + n - 1
        j = n - 1

        while indx >= 0 and j >= 0:
            if nums1[indx] == 0:
                indx -= 1
            elif nums1[indx] > nums2[j]:
                nums1[i] = nums1[indx]
                i -= 1
                indx -= 1
            elif nums1[indx] <= nums2[j]:
                nums1[i] = nums2[j]
                i -= 1
                j -= 1
        
        if j > -1:
            nums1[:i+1] = nums2[:j+1]
