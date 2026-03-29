class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = sum(nums)
        n = len(nums)
        return (n*(n+1) // 2) - x