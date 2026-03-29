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
            subset.append(nums[i])
            backtrack(i, curr+nums[i])
            subset.pop()
            backtrack(i+1, curr)

        backtrack(0,0)
        return res
        