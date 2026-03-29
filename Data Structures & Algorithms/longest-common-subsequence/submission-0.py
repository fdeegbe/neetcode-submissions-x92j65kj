class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        # 2d DP

        def dfs(row,col):
            if row == len(text1) or col == len(text2):
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            elif text1[row] == text2[col]:
                memo[(row,col)] = 1 + dfs(row+1, col+1)
            else:
                memo[(row,col)] = max(dfs(row+1, col), dfs(row, col+1))
            return memo[(row,col)]
        dfs(0,0)
        return memo[(0,0)]