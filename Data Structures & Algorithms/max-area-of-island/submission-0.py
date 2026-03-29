class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # is this # of islands but counting max area?
        # if you start from the middle, how do you keep track of the sum?
        res = 0
        def dfs(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    return (1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1))
            return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res, dfs(r,c))
        return res