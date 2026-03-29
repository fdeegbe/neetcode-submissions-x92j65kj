# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, high):
            nonlocal count
            if not root:
                return
            if root.val >= high:
                count += 1
                high = root.val
            dfs(root.right, high)
            dfs(root.left, high)
        dfs(root, root.val)
        return count