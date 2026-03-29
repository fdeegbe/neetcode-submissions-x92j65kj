class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n < 3:
            return dp[n-1]

        for i in range(2,n):
            dp.append(dp[-1] + dp[-2])

        return dp[n-1]
            
