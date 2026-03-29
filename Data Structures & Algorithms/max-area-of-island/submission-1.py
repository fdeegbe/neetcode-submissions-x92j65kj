class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        memo = {}
        res = 0
        def dfs(row,col):
            print((i,j))
            if (row,col) in memo:
                return 0 
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                memo[(row,col)] = True
                if grid[row][col] == 1:
                    print("HIT")
                    return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
                return 0
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(dfs(i,j), res)
        return res