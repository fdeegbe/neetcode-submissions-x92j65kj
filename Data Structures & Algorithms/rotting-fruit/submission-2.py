class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs does not need a proiority queue...
        q = deque()
        moves = [[0,1], [1,0], [-1,0], [0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((0, i, j))
        res = 0
        while q:
            minute, i, j = q.popleft()
            for dx, dy in moves:
                ix, jy = i + dx, j + dy
                if min(ix,jy) >= 0 and ix != len(grid) and jy != len(grid[0]):
                    if grid[ix][jy] == 1:
                        grid[ix][jy] = 2
                        q.append((minute+1,ix,jy)) 
                        res = max(res,minute+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return res