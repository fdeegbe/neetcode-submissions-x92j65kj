class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # trees are acylic, so khan's algo works here, as long as we dont go backward on our bfs.
        # how do we do this is bfs/dfs?
        # use a visited memo, and you add the adj bidirectionally
        # if it is visited(and not the parent) it is okay
        # bfs/dfs should reach the entire scc (since it is undirected)
        # we knew toposort could solve this, but knowing dfs/bfs method is a bit simpler (and good to know)
        adj = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            if u == v:
                return False

        def dfs(u, parent):
            res = True
            visited[u] = True
            print(u, adj[u])
            for nei in adj[u]:
                if nei != parent:
                    if not visited[nei]:
                        print(nei,visited)
                        res |= dfs(nei, u)
                    else:
                        print("Fail")
                        return False
            return res
        # A tree is a SCC
        if not dfs(0,0):
            return False
        else:
            return all(visited)
                    
            