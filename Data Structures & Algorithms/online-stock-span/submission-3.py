class StockSpanner:

    def __init__(self):
        self.prices = []
        self.Ndays = 0

    def next(self, price: int) -> int:
        # add new price to prices
        self.prices.append(price)       
        self.Ndays += 1                
        
        # calculating days back were conditions met
        daysBack = 1          
        for i in range(self.Ndays - 2, -1, -1): 
            if self.prices[i] <= price:  
                daysBack += 1                       
            else:
                break
        return daysBack        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)