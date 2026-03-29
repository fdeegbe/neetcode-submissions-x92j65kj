class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # use a set, keep track of the index
        count = nums[0]
        for i in range(len(nums)):
            if i > count:
                return False
            count = max(count, i+nums[i]) # get the biggest jump
        return True