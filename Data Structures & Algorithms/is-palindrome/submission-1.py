class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")):
                stack.append(c.lower())
        
        n = 0
        copy_stack = stack[:]
        while len(copy_stack) > 0:
            print(copy_stack)
            if copy_stack[0] == copy_stack[-1]:
                copy_stack = copy_stack[1:-1]
            else:
                return False
        return True
        
        