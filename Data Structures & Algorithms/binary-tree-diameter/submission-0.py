# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# get the maximum sum of the left and right child in the tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lst = []
        print("HI")

        def depth(node):
            if node:
                return max(depth(node.left), depth(node.right))+1
            return 0

        def calculateMax(node, height=0):
            if not node:
                return
            print(depth(node.left))
            print(depth(node.right))
            lst.append(depth(node.left) + depth(node.right))
            calculateMax(node.left)
            calculateMax(node.right)
            return
        print("hell")
        calculateMax(root)
        return max(lst)

            