class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        remaining = strs[:]
        output = []

        while remaining:
            word = remaining[0]
            subOutput = [word]
            remaining.remove(word)

            
            for w in remaining[:]:
                if sorted(w) == sorted(word):
                    subOutput.append(w)
                    remaining.remove(w)

            output.append(subOutput)
        return output
