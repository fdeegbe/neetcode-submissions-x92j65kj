class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        curr = 0
        for i in nums:
            curr += i
            res = max(res,curr)
            if curr < 0:
                curr = 0
        return res