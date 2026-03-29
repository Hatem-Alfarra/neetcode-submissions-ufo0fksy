class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r1 = m - 1
        r2 = n - 1
        indx = r1 + r2 + 1
        
        while indx >= 0 and r1 >= 0 and r2 >= 0:
            if nums1[r1] > nums2[r2]:
                nums1[indx] = nums1[r1]
                r1 -= 1
                indx -= 1
            else:
                nums1[indx] = nums2[r2]
                r2 -= 1
                indx -= 1
        
        nums1[:r2+1] = nums2[:r2+1]
        
