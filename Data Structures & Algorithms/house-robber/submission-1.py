class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # Precompute the first two solutions
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2,len(nums)):
            dp.append(max(dp[i-2]+nums[i], dp[i-1]))
        print(dp)

        return dp[-1]