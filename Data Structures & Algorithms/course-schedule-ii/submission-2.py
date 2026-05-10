class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        visited = []
        path = []

        def dfs(cl):
            if cl in visited:
                return False
            if cl in path:
                return True
            visited.append(cl)
            for neigh in graph[cl]:
                if not dfs(neigh):
                    return False
            path.append(cl)
            visited.pop()
            return True

        for cl in range(numCourses):
            if not dfs(cl):
                return []
        return path

            
            


        