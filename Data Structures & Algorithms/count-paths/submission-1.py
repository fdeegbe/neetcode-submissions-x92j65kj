class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        COLS = m
        ROWS = n
        memo = [1] * COLS
        # print(memo)
        for j in range(ROWS-1):
            for i in range(1, COLS):
                memo[i] = memo[i] + memo[i-1]
            # print(memo)
        return memo[-1]
