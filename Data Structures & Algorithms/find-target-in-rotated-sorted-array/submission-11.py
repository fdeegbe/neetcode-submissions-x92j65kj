class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # same stuff, we know the ranges, so if the number is between left and middle, seach that side and vice versa
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l) // 2
            print(l, m, r, nums[l:r+1])
            # if the target is on the left side, search left otherwise, search right
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]: #correct interval
                if nums[l] <= target < nums[m]:
                    # search left
                    r = m-1
                else:
                    l = m+1
            else: # correct interval
                if nums[m] < target <= nums[r]:
                    # search the right side
                    l = m+1
                else:
                    r = m-1
        return -1

        # return -1 if nums[l] != target else l