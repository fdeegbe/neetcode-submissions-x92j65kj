"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        memo = {} # this is a mapping from old values to new ones... because it's easier that way

        def dfs(node):
            if node in memo:
                return memo[node]
            copy = Node(node.val)
            memo[node] = copy
            for c in node.neighbors:
                copy.neighbors.append(dfs(c))
            return copy
        return dfs(node) if node else None

