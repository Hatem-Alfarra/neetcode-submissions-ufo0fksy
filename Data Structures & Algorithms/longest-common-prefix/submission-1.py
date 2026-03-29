class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        
        
        for word in strs[1:]:
            n = 0
            while (word[:n+1] == common[:n+1]) and (n<=len(common)):
                n += 1
            common = common[:n]
        
        return common