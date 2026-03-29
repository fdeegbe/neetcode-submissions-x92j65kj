class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        l, r = 1, nums[0]
        jumps = 1
        # slding window, save the largest next value in the interval
        while r < len(nums)-1:
            nextBiggest = 0
            while l <= r and l<len(nums): # find the furthest you can reach
                nextBiggest = max(nextBiggest, l+nums[l])
                print(nextBiggest)
                l+=1
            r = nextBiggest # advance r
            jumps += 1
            print("JUMP",l,r)
        return jumps