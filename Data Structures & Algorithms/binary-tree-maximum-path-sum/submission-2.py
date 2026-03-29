# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        lmax = float('-inf')
        # we can go to the local max, and just get the max of bothj sides via bottom=-up recursion
        def dfs(root, maximum=0, cumsum=0):
            nonlocal lmax
            if root is None:
                return 0
            # max - if the left leaf's value is negative-restart at 0
            l = dfs(root.left)
            r = dfs(root.right)
            maximum = max(l, r, 0) + root.val
            print("Node :", root.val)
            print("lmax :", maximum)
            lmax = max(lmax, l+r+root.val, maximum)
            return maximum
            # take the val, or end the tree?
            # we can hold the cumsum, and reset it when it becomes negative
        dfs(root)
        print(lmax)
        return lmax
        