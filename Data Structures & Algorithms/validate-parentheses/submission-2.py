class Solution:
    def isValid(self, s: str) -> bool:
        my_list = []
        openings = {0:'(', 1:'{', 2:'['}
        closings = {')':0, '}':1, ']':2}

        for char in s:
            if char in openings.values():
                my_list.append(char)
            else:
                if (my_list):
                    if my_list[-1] == openings[closings[char]]:
                        my_list.pop()
                    else:
                        return False
                else:
                    return False
        if (my_list):
            return False
        return True