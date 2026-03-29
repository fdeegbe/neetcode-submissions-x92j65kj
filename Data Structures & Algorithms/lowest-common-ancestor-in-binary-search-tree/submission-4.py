# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        def dfs(root):
            nonlocal p, q, res
            print(root.val)
            # no need for a base case
            if p.val > root.val and q.val > root.val: # go right
                dfs(root.right)
            elif p.val < root.val and q.val < root.val: # go left
                dfs(root.left)
            else: # else, they split
                res = root
            return
        dfs(root)
        return res


