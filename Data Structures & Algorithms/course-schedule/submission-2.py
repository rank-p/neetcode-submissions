class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for u,v in prerequisites:
            # [0,1] represents 1 -> 0
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque()
        q.extend([i for (i,count) in enumerate(indegree) if count == 0])

        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            
            neighbors = graph[curr]
            for n in neighbors:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        return len(order) == numCourses
