# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            new = None
            if node: 
                new = TreeNode(node.val)
                new.left = reverse(node.right)
                new.right = reverse(node.left)

            return new
        new = reverse(root)
        return new