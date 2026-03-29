class Solution:
    def rob(self, nums: List[int]) -> int:
        # if you rob the curent house, you cant rob the house behind you.
        # sum 1
        if len(nums) < 3:
            return max(nums)
        n = len(nums)
        memo = [-1] * n
        memo[0] = nums[0]
        memo[1] = max(nums[1], nums[0])
        for i in range(2,n):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i])
        print(memo)
        return max(memo[n-1], memo[n-2])