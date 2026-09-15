class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_buy = prices[0]
        max_profit = 0
        for (i,price) in enumerate(prices):
            profit = price-min_buy
            max_profit = max(max_profit,profit)

            min_buy = min(min_buy, price)
        
        return max_profit
        