# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # keep track of the range of numbers each child is within, and validate as u go down
        # the first one should be fro [-inf to inf] 
        # left ought ta be [-inf to parent.val] right ought ta be [parent.val to inf]
        def validate(root, left_bound, right_bound):
            if not root:
                return True
            if not left_bound < root.val < right_bound:
                # print(root.val, left_bound, right_bound)
                return False
            return validate(root.left, left_bound, root.val) and validate(root.right, root.val, right_bound)
        #call fxn 
        return validate(root, float('-inf'), float('inf'))