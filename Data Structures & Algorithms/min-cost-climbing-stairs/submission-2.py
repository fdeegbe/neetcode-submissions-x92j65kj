class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost
        memo = [-1] * len(cost)
        def dfs(n): # n is the step youre on, the memo will keep track of the smallest cost you can get at that step
            if n >= len(cost):
                return 0
            if memo[n] != -1:
                return memo[n]
            memo[n] = cost[n] + min(dfs(n+1), dfs(n+2))
            return memo[n]
        dfs(0)
        # print(memo)
        return min(dfs(0), dfs(1))