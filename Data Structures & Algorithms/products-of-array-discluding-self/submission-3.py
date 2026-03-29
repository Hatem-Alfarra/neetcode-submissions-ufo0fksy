class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        res = []

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                prod *= num
        
        for num in nums:
            if zeros > 1:
                res.append(0)
            elif num == 0:
                res.append(prod)
            elif num and zeros:
                res.append(0)
            else:
                res.append(int(prod/num))

        return res