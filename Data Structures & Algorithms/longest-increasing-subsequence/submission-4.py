class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n
        nums.reverse()

        memo[0] = 1
        for i in range(1,n):
            for j in range(0,i):
                if nums[j] > nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)
        print(memo)
        return max(memo)


