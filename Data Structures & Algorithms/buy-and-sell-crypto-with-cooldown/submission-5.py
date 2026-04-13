from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # decision problem for boy, sell, or do nothing you can only do nothing if you sdell and tuple of index, buy/sell
        if len(prices) <= 1:
            return 0


        @lru_cache(None)
        def dfs(i, cooldown):
            # Buy: Cooldown 1
            # sell, Cooldown 2
            # cooldown: buy, sell 3
            if i >= len(prices):
                return 0

            buy = 0
            sell = 0
            skip = 0
            if cooldown != 1:
                buy = dfs(i+1, 1) - prices[i]
            if cooldown == 1:
                sell = dfs(i+2, 0) + prices[i]
            skip = dfs(i+1, cooldown)
            return max(buy,sell,skip)
            
        return dfs(0, 0)