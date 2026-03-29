class Solution:
    def findMin(self, nums: List[int]) -> int:
        # arrays that have been rotated have certain properties.. 
        # you can binary search them 
        # l should be <= m < r
        # if they arent, we can find the splitting point eassier.

        # next time we get this type of problem, think about the properties of a rotated array
        # and think about how we can create a split between the two, making two sorted arrays on each side,
        # or one big sorted array.

        # now, also keep in mind that it is possible to binary search a rotated array in log(n) time

        # cheers.

        l, r = 0, len(nums)-1
        m = l + (r -l) // 2

        while l <= r:
            if nums[l] > nums[m]: # this is not correct, so we need to search this side of thwe array, as this is where the split must be.
                r = m # move r to search left side
                print(nums[l:r], l ,r, m)
            elif nums[r] <= nums[m]: # this should never hold, so we need to search this side of the array..
                l = m + 1 # move l to search right
                print(nums[l:r], l ,r, m)
            else: # if the array is sorted now, we can take l (the smallest element)
                print(nums[l:r], l ,r, m)
                return nums[l]
            m = l + (r -l) // 2
        print(l, m, r)
        return nums[m]
