class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t = 1
        post = 1
        pre = []
        for i in range(len(nums)):
            pre.append(t)
            t *= nums[i]
        res = []
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res.append(pre[i] * post)
            post *= nums[i]
        return res[::-1]
