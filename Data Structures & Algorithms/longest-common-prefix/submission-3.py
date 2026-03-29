class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        for word in strs[1:]:
            n = 0
            while (len(word)> n <len(common)) and  (word[n] == common[n]):
                n += 1
            common = common[:n]
        
        return common