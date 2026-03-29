# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []
        def dfs(root, depth):
            nonlocal level
            if not root:
                return None
            if len(level) == depth:
                level.append([])
            
            level[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return level
            
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     queue = [root]
    #     solution = []
    #     while queue:
    #         level = []
    #         qlen = len(queue)
    #         for _ in range(qlen):
    #             elem = queue.pop(0)
    #             level.append(elem.val)

    #             if elem.left:
    #                 queue.append(elem.left)
    #             if elem.right:
    #                 queue.append(elem.right)

    #         solution.append(level)
    #     # print(solution)
    #     return(solution)
            

        