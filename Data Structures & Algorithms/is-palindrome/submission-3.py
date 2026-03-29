class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        s = s.lower()

        for char in s:
            if ord("a") <= ord(char) <= ord("z") or ord("0") <= ord(char) <= ord("9"):
                clean.append(char)
        
        length = len(clean)
        for i in range(length//2):
            if clean[i] != clean[-i-1]:
                return False
        return True