# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find(root, target, lst):
            lst.append(root)
            if target > root.val: # search right
                find(root.right, target, lst)
            elif target < root.val: #search left
                find(root.left, target, lst)
            else:
                return
        qlst = []
        plst = []
        find(root, q.val, qlst)
        find(root, p.val, plst)
        # qlst.reverse()
        # plst.reverse()
        for i in range(min(len(qlst), len(plst))):
            if qlst[i].val != plst[i].val:
                return qlst[i-1]
        # print(plst, qlst)
        # i = 0
        # while qlst[i].val == plst[i].val:
        #     i += 1
        return qlst[i]


