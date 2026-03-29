class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for elem in nums:
            temp = res.copy()
            for i in range(len(temp)):
                temp[i] = temp[i].copy()
                temp[i].append(elem)
            res.extend(temp)
        return res