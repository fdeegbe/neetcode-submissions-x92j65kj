class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        nums.sort()

        def backtrack(i, curr):
            print(subset)
            if i >= len(nums) or curr > target:
                return
            if curr == target:
                res.append(subset.copy())
                return
            for j in range(i, len(nums)):
                if curr + nums[j] > target:
                    return
                subset.append(nums[j])
                backtrack(j, curr + nums[j])
                subset.pop()

        backtrack(0,0)
        return res
        