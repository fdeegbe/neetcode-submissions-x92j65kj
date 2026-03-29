# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def inorder(root, lst):
            if root:
                inorder(root.left, lst)
                inorder(root.right, lst)
                lst.append(root.val)
        lst1 = []
        lst2 = []
        inorder(root, lst1)
        inorder(subRoot, lst2)
        print(lst1,lst2)
        return lst1[:len(lst2)] == lst2
