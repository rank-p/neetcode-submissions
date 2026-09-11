class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for (u,v) in prerequisites:
            # v -> u
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque()
        for (course, degree) in enumerate(indegree):
            if degree == 0:
                q.append(course)
        
        # BFS
        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return len(order) == numCourses
        