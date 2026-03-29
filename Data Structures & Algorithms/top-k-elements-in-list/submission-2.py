class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for elem in nums:
            dic[elem] += 1
        res = []
        # return list(list(zip(*sorted(dic.items(), reverse=True, key=lambda x: x[0])))[0][:k])
        for val, count in dic.items():
            res.append((count, val))
        res.sort(reverse=True, key=lambda x: x[0])
        # print(res)
        return [b for a,b in res][:k]
