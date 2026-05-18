class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We definitely need to buy when it's the lowest and sell at the maximum price 
        smallest_num = prices[0]
        profit = 0
        for i in prices[1:]: 
            if i < smallest_num: 
                smallest_num = i 
            else: 
                profit = max(profit, i - smallest_num)
        return profit 