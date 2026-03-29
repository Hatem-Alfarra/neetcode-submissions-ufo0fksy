class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        maxSell, minBuy = -1, prices[0]
        days = len(prices)

        for day in range(days):
            if prices[day] < minBuy:
                minBuy = prices[day] 
                maxSell = -1
            if prices[day] > maxSell: 
                maxSell = prices[day] 
                dif = maxSell - minBuy
                if dif > maxP:
                    maxP = dif
        
        return maxP
            

