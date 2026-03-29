class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # prim's algo (starts at a source)
        mstSet = [False] * (n+1)
        res = [None] * (n+1)
        key = [float('inf')] * (n+1) # used to pick what node should go next (the smallest value not already in our mst)
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

        key[k] = 0 # start with k
        res[k] = 0
            

        # time to start
        for _ in range(n):
            curr = getNext()
            if curr == 0:
                return -1

            mstSet[curr] = True

            for nei, time in adj[curr]:
                if key[nei] > key[curr] + time:
                    key[nei] = key[curr] + time
            
        # print(key, res)
        return max(key[1:])
                

        