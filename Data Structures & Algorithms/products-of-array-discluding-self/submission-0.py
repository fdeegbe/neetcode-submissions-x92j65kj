class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t = 1
        pre = []
        res = []
        for i in range(len(nums)):
            pre.append(t)
            t *= nums[i]
        print(pre)
        post = 1
        for i in range(len(nums)-1,-1,-1):
            print(pre[i], post)
            res.append(pre[i] * post)
            post *= nums[i]
        return res[::-1]
