# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q) or (q == None and p):
            return False
        if not p and not q:
            return True
        print(p.val, q.val)
        val = True
        val &= self.isSameTree(p.left, q.left)
        val &= self.isSameTree(p.right, q.right)

        if p.val == q.val:
            return val
        return False