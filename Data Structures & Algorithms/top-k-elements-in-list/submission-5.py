class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = {}

        for val in nums:
            if val in frequencyDict:
                frequencyDict[val] += 1
            else:
                frequencyDict[val] = 1

        valDict = {} 
        for val, freq in frequencyDict.items():
            if freq in valDict:           
                valDict[freq].append(val)  
            else:
                valDict[freq] = [val]
            
        
        sortedValDict = dict(sorted(valDict.items(), reverse=True))
        sortedValList = list(sortedValDict.values())

        ans = []
        for _ in range(k):
            top = sortedValList[0][0]
            sortedValList[0] = sortedValList[0][1:]
            if sortedValList[0] == []:
                sortedValList = sortedValList[1:]

            ans.append(top)

        return ans
