# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # actually preorder
        def inorder(root, lst):
            if root:
                inorder(root.left, lst)
                inorder(root.right, lst)
                lst.append(root.val)
        if not subRoot:
            return True
        lst1 = []
        lst2 = []
        inorder(root, lst1)
        inorder(subRoot, lst2)
        print(lst1,lst2)

        # for i in range(len(lst1)):
        #     if lst1[i] == lst2[0]:
        #         if lst1[i: i+len(lst2)] == lst2:
        #             return True
        return lst1[:len(lst2)] == lst2
