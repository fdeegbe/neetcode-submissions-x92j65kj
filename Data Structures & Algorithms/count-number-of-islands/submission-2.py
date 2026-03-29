class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs routine - change all 1's to 0's in a flood fill and then ur done ig
        def dfs(row,col):
            # print("hi")
            if 0 <= col < len(grid[0]) and 0 <= row < len(grid):
                # print("bruh")
                if grid[row][col] == '1':
                    # print("bruhhelious")
                    grid[row][col] = '0'

                    dfs(row+1,col)
                    dfs(row-1,col)
                    dfs(row,col+1)
                    dfs(row,col-1)
                    return True

            return False
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # print(row,col, grid[row][col])
                if dfs(row,col):
                    count+=1
        return count
