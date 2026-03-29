class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indeg = {c:0 for w in words for c in w}
        # toposort?
        adj = defaultdict(set)
        # construct the graph
        for i in range(len(words)-1):
            pair1, pair2 = words[i], words[i+1]
            minlen = min(len(pair1), len(pair2))
            if len(pair1) > len(pair2) and pair1[:minlen] == pair2[:minlen]:
                return ""
            for j in range(minlen):
                p1 = pair1[j]
                p2 = pair2[j]
                if p1 != p2:
                    if p2 not in adj[p1]:
                        print(p1,p2)
                        adj[p1].add(p2)
                        indeg[p2] += 1
                    break
        print(adj)

        res = []
        q = [c for c in indeg.keys() if indeg[c] == 0]
        print(indeg, q)
        while q:
            curr = q.pop()
            for nei in adj[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
            res.append(curr)
        print(res)
        if len(res) != len(adj):
            return ""
        return ''.join(res)


