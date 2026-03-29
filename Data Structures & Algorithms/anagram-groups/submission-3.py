class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dictionary = {} 
        for word in strs: 
            ordered = str(sorted(word)) 
            if ordered in my_dictionary:
                my_dictionary[ordered].append(word)
            else:
                my_dictionary[ordered] = [word]
        solution = []
        for group in my_dictionary.values():
            solution.append(group)
        return solution
            
        