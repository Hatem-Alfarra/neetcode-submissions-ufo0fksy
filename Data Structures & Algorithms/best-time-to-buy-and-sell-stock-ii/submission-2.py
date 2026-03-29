class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        left = prices[0]

        for day in range(1, len(prices)):   
            if prices[day] < left:
                left = prices[day]
            if prices[day] > left:
                profits += prices[day] - left
                left = prices[day]
        
        return profits
            

