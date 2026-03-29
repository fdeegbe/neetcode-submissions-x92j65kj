class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        nums.sort()
        def dfs(i, curr):

            if curr == target:
                res.append(subset.copy())
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if curr + nums[j] > target:
                    break
                subset.append(nums[j])
                dfs(j+1, curr+nums[j])
                subset.pop()

        dfs(0,0)
        return res