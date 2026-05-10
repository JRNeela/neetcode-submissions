class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        #graph filled with each class and their values are their respective prereqs
        finished = []
        inProcess = []
        def dfs(course):
            if course in finished:
                return True
            if course in inProcess:
                return False
            inProcess.append(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            finished.append(course)
            inProcess.pop()
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
