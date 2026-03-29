class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        days = len(prices)
        left = prices[0]

        for day in range(1, days):   
            if prices[day] < left:
                # buy
                left = prices[day]
            if prices[day] > left:
                # sell
                profits += prices[day] - left
                left = prices[day]
        
        return profits
            

