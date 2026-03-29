class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + ((r-l) // 2)
            if nums[m] < target: #choose bigger half
                l = m+1
            elif nums[m] > target: # choose smaller half
                r = m-1
            else:
                return m
        return -1
