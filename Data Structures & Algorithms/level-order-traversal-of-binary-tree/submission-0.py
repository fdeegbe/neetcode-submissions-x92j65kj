# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        solution = []
        while queue:
            level = []
            for _ in range(len(queue)):
                elem = queue.pop(0)
                level.append(elem.val)

                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)

            solution.append(level)
        # print(solution)
        return(solution)
            

        