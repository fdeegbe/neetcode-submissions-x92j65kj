class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # maintain a set of pac and atl oceans, with their positions.
        # bfs, and get all of the nodes that are bigger than it
        pac = set()
        atl = set()
        visited = set()

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def inBounds(row, col):
            if row in range(len(heights)) and col in range(len(heights[0])):
                return True
            return False

        def dfs(row,col, ocean):
            # no need for input validation
            curr = heights[row][col]
            ocean.add((row,col))
            visited.add((row,col))
            for x, y in directions:
                rowx = row + x
                coly = col + y
                if inBounds(rowx, coly) and heights[rowx][coly] >= curr and (rowx, coly) not in visited:
                    dfs(rowx,coly, ocean)
            return


        for col in range(len(heights[0])):
            dfs(0,col, pac)
            visited = set()
            dfs(len(heights)-1, col, atl)
            visited = set()
        for row in range(len(heights)):
            dfs(row,0, pac)
            visited = set()
            dfs(row, len(heights[0])-1, atl)
            visited = set()
        print(pac, atl, pac.intersection(atl))
        return list(pac.intersection(atl))

