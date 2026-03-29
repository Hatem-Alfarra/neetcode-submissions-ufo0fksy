class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            temp = t
            t = s
            s = temp
        for substring_s in s:
            if substring_s in t:
                t = t.replace(substring_s, "", 1)
            else:
                return False
        return True
        