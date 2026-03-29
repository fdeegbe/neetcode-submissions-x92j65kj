class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        memo[0], memo[1] = cost[0], cost[1]
        for i in range(2,len(cost)):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])
        # print(memo) 1 2 2 4 3 4 4
        return min(memo[-1], memo[-2])