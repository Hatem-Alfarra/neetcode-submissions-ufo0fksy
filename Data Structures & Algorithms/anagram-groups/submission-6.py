class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupsDict = {}
        for word in strs:
            sortedWord = str(sorted(word))
            if sortedWord in groupsDict:
                groupsDict[sortedWord].append(word)
            else:
                groupsDict[sortedWord] = [word]
        
        return list(groupsDict.values())