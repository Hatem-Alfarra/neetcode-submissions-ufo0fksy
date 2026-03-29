class Solution:
    def mySqrt(self, x: int) -> int:
        h = x // 2

        for i in range(h+1):
            j = i*i
            if j == x:
                return i
            elif j > x:
                return i - 1
        return 1