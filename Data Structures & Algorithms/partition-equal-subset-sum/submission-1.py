class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tgt = sum(nums)
        if tgt % 2:
            return False
        tgt = tgt / 2
        memo = set([0])

        for i in nums:
            temp = set()
            for elem in memo:
                if elem + i == tgt:
                    return True
                elif elem + i < tgt:
                    temp.add(elem + i)
            memo = memo.union(temp)
        return False
