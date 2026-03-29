# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# do an inorder traversal bc its sorted lol 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, lst):
            if not root:
                return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right,lst)
        res = []
        inorder(root, res)
        return res[k-1]