class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lastIdx = len(nums)-1
        while lastIdx >= 0 and nums[lastIdx] == val:
            lastIdx -= 1
        
        i = 0
        while i < lastIdx:
            if nums[i] == val:
                nums[i], nums[lastIdx] = nums[lastIdx], nums[i]
                while lastIdx >= 0 and nums[lastIdx] == val:
                    lastIdx -= 1
            i+=1
        return lastIdx + 1