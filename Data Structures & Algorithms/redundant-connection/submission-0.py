class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]
        deg = [0 for _ in range(len(edges)+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u]+=2
            deg[v]+=2
        print(adj, deg)

        q = deque([i for i in range(1,len(edges)+1) if deg[i] == 2])
        print("q: ",q)
        res = set()
        while q:
            curr = q.popleft()
            deg[curr] -=2
            for nei in adj[curr]:
                deg[nei] -= 2
                if deg[nei] == 2:
                    q.append(nei)
            res.add(curr)
        print(res)
        for i in range(len(edges)-1,-1,-1):
            u,v = edges[i]
            if u in res or v in res:
                continue
            else:
                return [u,v]
            
