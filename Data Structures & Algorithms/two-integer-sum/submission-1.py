class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in memo:
                return [memo[difference], i]
            memo[nums[i]] = i