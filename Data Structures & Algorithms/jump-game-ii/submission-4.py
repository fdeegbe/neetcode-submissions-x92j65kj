class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        jumps = 1
        l = 1
        r = nums[0]

        while r < len(nums)-1:
            reach = 0
            for i in range(l,r+1):
                if i < len(nums):
                    reach = max(reach,i + nums[i])
            l = r + 1
            r = reach
            jumps +=1
        return jumps
        