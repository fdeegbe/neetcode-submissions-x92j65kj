
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # use a map to go from old to new
        memo = {}
        def dfs(root):
            if root in memo:
                return memo[root]
            if not root:
                return root
            node = memo.get(root, Node(root.val))
            memo[root] = node
            for chld in root.neighbors:
                node.neighbors.append(dfs(chld))
            return node
        return dfs(node)