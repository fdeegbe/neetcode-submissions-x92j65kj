class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # toposort, khans algo for cycle detection
        # array instead of defaultdict slightly more space efficent - no need to change hashing algorithims
        adj = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
            indeg[u] += 1 # keep track of in degrees

        q = deque([c for c in range(len(indeg)) if indeg[c] == 0])
        res = 0
        while q:
            curr = q.popleft()
            res += 1
            for neighbor in adj[curr]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)
        return res == numCourses

            

