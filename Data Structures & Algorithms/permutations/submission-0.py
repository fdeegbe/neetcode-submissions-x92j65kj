class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []


        def bfs(i,usable):
            # print(subset)
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for j in range(0, len(nums)):
                if nums[j] in usable:
                    subset.append(nums[j])
                    usable.remove(nums[j])

                    bfs(j, usable)
                    
                    subset.pop()
                    usable.add(nums[j])
            return
        bfs(-1, set(nums))
        return res