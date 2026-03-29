class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set() # this will emulate a "per path memo table",
        # as long as we remove the element we add after processing.
        # populate adj list
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        print(graph)
        def dfs(c):

            if c not in graph:
                return True

            if c in visited:
                return False 

            visited.add(c)
            for nc in graph[c]:
                res = dfs(nc)
                if not res:
                    return False
            visited.remove(c)
            # another optiization: we can remove the current element after recursion if we know it has no cycles.
            del graph[c]

            return True
        # def end
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



