class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        def dfs(n):
            if n < 3:
                memo[n] = n
                return memo[n]
            if memo[n] != -1:
                return memo[n]
            memo[n] = dfs(n-1) + dfs(n-2)
            # print(memo, memo[n])
            return memo[n]
        dfs(n)
        # print(memo)
        return memo[n]
        