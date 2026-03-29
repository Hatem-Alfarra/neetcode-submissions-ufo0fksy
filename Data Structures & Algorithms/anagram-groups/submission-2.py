class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for s in strs:
            s_sorted = tuple(sorted(s))
            if s_sorted in my_dict.keys():
                my_dict[s_sorted].append(s)
            else:
                my_dict[s_sorted] = [s]
        
        return list(my_dict.values())
