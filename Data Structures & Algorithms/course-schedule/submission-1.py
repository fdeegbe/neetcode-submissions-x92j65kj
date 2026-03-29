class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # keep track of cycle detection, visited set, and go through visited nodes
        res = False
        visited = set()
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        # created adj list, need dfs routine
        def dfs(node, local_visited):
            # traverse to reacable nodes
            # mark visited localized
            # return that, to be added to the global
            if not graph[node]:
                return True

            # print(node)
            # print(local_visited)
            if node in local_visited:
                # Cycle detected
                return False

            # add to visited set
            local_visited.add(node)
            # visited.add(node)

            # check if node is in visited set (localized)
            for child in graph[node]:
                # traverse
                if not dfs(child, local_visited):
                    return False
            return True

        for course in range(numCourses):
            # if course not in visited:
            if not dfs(course, set()):
                return False
        return True



