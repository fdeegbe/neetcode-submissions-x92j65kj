class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs with a visited list to find the sccs
        # have to use a parent pointer'
        adj = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(n, parent):
            visited[n] = True
            ret = True
            for nei in adj[n]:
                if nei != parent:
                    if not visited[nei]:
                        ret |= dfs(nei,n)
            return ret
        ret = 0
        for i in range(n):
            if not visited[i]:
                dfs(i,i)
                ret += 1
        return ret
                    