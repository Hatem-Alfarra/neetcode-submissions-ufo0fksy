class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: [0], 10: [0], 20: [0]}

        for bill in bills:
            if bill == 5:
                change[5][0] += 1
            elif bill == 10:
                if change[5][0] >= 1:
                    change[5][0] -= 1
                    change[10][0] += 1
                else:
                    return False
            else:
                if change[10][0] >= 1:
                    if change[5][0] >= 1:
                        change[10][0] -= 1
                        change[5][0] -= 1
                        change[20][0] += 1
                    else:
                        return False
                elif change[5][0] >= 3:
                    change[5][0] -= 3
                    change[20][0] += 1
                else:
                    return False

        return True