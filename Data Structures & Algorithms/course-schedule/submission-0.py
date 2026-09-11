class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        g = defaultdict(list)
        for (u,v) in prerequisites:
            indegree[u] += 1
            g[v].append(u)
                
        q = deque()
        for course, count in enumerate(indegree):
            if count == 0:
                q.append(course)
            

        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for neighbor in g[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
    
        return len(order) == numCourses
        