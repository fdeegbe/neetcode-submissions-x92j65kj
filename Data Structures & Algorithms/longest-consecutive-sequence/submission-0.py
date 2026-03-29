class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store into a set and count consec
        lst = set(nums)
        ret = 0
        for i in lst:
            if i-1 in lst:
                continue
            curr = i
            temp = 1
            while curr + 1 in lst:
                temp += 1
                curr +=1
            ret = max(ret, temp)
        return ret
                
            
        