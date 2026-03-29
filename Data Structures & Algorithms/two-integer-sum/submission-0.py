class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ref:
                return [ref[diff], i]
            else:
                ref[nums[i]] = i
        
        