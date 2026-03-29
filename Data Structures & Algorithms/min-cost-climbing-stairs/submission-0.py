class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost + [0] + [0]
        memo = [-1] * (len(cost)+1)
        def dfs(n): # n is the step youre on, the memo will keep track of the smallest cost you can get at that step
            if n >= len(cost)-2:
                return 0
            if memo[n] != -1:
                return memo[n]
            memo[n] = min(dfs(n+1) + cost[n+1], dfs(n+2) + cost[n+2])
            return memo[n]
        dfs(0)
        print(memo)
        return memo[0]