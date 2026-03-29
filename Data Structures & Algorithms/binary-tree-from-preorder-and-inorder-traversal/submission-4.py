# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        node = preorder[0]
        print("placing node ", node)
        root = TreeNode(node)
        idx = inorder.index(node)
        in1 = inorder[:idx]
        in2 = inorder[idx+1:]
        print("dump: ", preorder, inorder)
        pre1 = preorder[1:len(in1)+1]
        pre2 = preorder[len(in1)+1:]
        print(pre1, pre2)
        print(in1, in2)
        # print(idx)
        root.left = self.buildTree(pre1, in1)
        root.right = self.buildTree(pre2, in2)
        return root