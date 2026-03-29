class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob(i,last=False):
        # last = can take the last value
            dp = [-1] * len(nums)
            dp[0],dp[1] = nums[0], max(nums[0],nums[1])
            if last:
                dp[0] = 0
                dp[1] = nums[1]
            for i in range(2,len(nums)):
                if i != len(nums)-1 or last:
                    dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            print(dp)
            return max(dp[-1],dp[-2])
        if len(nums) <= 3:
            return max(nums)
        return max(rob(1,False),rob(2,True))
        