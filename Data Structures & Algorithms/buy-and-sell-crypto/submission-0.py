class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        numDays = len(prices)

        for i in range(numDays):
            for j in range(i, numDays):
                dif = prices[j] - prices[i]
                if dif > maxProfit:
                    maxProfit = dif

        return maxProfit 