
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        # use a map to go from old to new
        memo = {}
        memo[node] = Node(node.val)

        q = deque([node])

        while q:
            curr = q.popleft()

            for chld in curr.neighbors:
                if chld not in memo:
                    memo[chld] = Node(chld.val)
                    q.append(chld) # add the child to the processing q (1 time only)
                memo[curr].neighbors.append(memo[chld])
        return memo[node]