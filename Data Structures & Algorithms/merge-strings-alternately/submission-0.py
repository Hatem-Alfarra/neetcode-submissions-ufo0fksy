class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        minLength = min(len(word1), len(word2))
        res = ""

        # loop throught both words intil i == minLength
        while i < minLength:
            res += word1[i] + word2[i]
            i += 1
        
        # add remaining from longer word
        if len(word1) > len(word2):
            res += word1[i:]
        else:
            res += word2[i:]

        return res