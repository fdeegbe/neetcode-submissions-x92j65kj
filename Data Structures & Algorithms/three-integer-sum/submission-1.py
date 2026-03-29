class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)-1
        res = []
        for i, e in enumerate(nums):
            # we only really need to go through 
            # the negative numbers near the start, 
            # as those are the only solutions that 
            # can produce a '0' result.
            if e > 0:
                break
            if i > 0 and e == nums[i-1]: # the starting elements are the same
                continue
            l = i+1
            r = n
            # sliding window search for answers
            while l < r:
                target = nums[l] + nums[r] + e
                if target == 0:
                    res.append([e,nums[l],nums[r]])
                    # append the pair and keep looking
                    # NOTE: You cannot have duplicate elements
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        # we move the left pointer until we find a new element
                        l+=1 
                    # we might as well also move the right pointer down,
                    # since theres no way the sum can be zero on the same iteration
                    r-=1
                elif target > 0:
                    r-=1
                else:
                    l+=1

        return res

        