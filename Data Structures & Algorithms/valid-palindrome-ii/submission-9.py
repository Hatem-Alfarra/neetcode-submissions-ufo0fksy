class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        oneDeleted = False

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] == s[r-1] and not oneDeleted:
                l += 1
                r -= 2
                oneDeleted = True
            else:
                break
        
        if l >= r:
            return True
        
        l, r = 0, len(s) - 1
        oneDeleted = False

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1    
            elif s[l+1] == s[r] and not oneDeleted:
                l += 2
                r -= 1
                oneDeleted = True
            else:
                break
        
        if l >= r:
            return True
    
        return False
            
        