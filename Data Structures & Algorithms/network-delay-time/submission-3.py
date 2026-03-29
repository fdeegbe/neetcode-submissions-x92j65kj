class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # prim's algo (starts at a source)
        mstSet = [False] * (n+1)
        res = [None] * (n+1)
        adj = defaultdict(list)
        for ui,vi,ti in times:
            adj[ui].append([vi,ti])
            # It might be startest to do adj matrix when dealing with this much data...

        def getNext(): # get next node to add to the MST
            smallest = float('inf')
            smallest_idx = 0
            for i in range(1,n+1):
                if not mstSet[i] and key[i] < smallest:
                    smallest = key[i]
                    smallest_idx = i
            return smallest_idx


        res[k] = 0
            
        pq = []
        pq.append((0,k))
        # time to start
        while pq:
            ti, ui = heapq.heappop(pq)
            if mstSet[ui]:
                continue
            res[ui] = ti

            mstSet[ui] = True

            print(pq,adj[ui])
            for nei, time in adj[ui]:
                if not mstSet[nei]:
                    heapq.heappush(pq, (ti + time, nei))
            
        # print(key, res)
        ans = -1
        for i in res[1:]:
            if i == None:
                return -1
            ans = max(ans,i)
        return ans
                

        