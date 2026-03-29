import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni, nj = newInterval[0], newInterval[1]
        start, end = 0,0
        res = []
        for i in range(len(intervals)):
            ti, tj = intervals[i]
            if ni <= ti <= nj:
                nj = max(nj, tj)
                continue
            elif ni <= tj <= nj:
                ni = min(ni, ti)
                continue
            elif ti < ni and tj > nj:
                nj = max(nj, tj)
                ni = min(ni, ti)
            else:
                res.append([ti,tj])
                
        bisect.insort_left(res,[ni,nj])
        return res