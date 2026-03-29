class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = maxProfit = maxR = 0
        minR = float('inf')
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit
                