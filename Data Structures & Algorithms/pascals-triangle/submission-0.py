class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        def generateHelper(lst):
            res = []
            res.append(1)
            for i in range(1, len(lst)):
                res.append(lst[i-1]+lst[i])
            res.append(1)
            return res
            
        res = []
        res.append([1])
        for _ in range(1, numRows):
            res.append(generateHelper(res[-1]))
            # print(res)
        return res
