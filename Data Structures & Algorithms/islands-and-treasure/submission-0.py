class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # route 1. take the min DFS at each chest, O(# of chests*n)
        # route 2. BFS. enqueue the shortest position
        # algo - min heap - store the distances and the position
        moves = [[1,0],[-1,0],[0,-1],[0,1]]
        q = []
        memo = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((0,i,j)) # mark where the zeroes are]

        while q:
            print(q)
            distance, i, j = heapq.heappop(q)
            for x, y in moves:
                xi = x+i
                yj = y+j
                if 0 <= xi < len(grid) and 0 <= yj < len(grid[0]):
                    print(xi,yj,distance)
                    if grid[xi][yj] == 2147483647:
                        grid[xi][yj] = distance + 1
                        heapq.heappush(q, (distance+1, xi, yj))
        print(grid)
        return None

