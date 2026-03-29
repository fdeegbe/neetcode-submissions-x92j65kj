class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        res = []
        for x, y in points:
            heapq.heappush(ans, (math.sqrt(x*x + y*y),(x,y)))
        for i in range(k):
            res.append(heapq.heappop(ans)[1])
        return res
