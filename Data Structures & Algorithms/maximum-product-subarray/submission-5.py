class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        res = 0
        currmax = currmin = 1
        for num in nums:
            tmp = currmax * num
            currmax = max(num, currmax*num, currmin*num)
            currmin = min(num, currmin*num, tmp)
            res = max(res,max(currmax, currmin))
        return res