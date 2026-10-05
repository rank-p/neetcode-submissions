class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        for course,pre in prerequisites:
            graph[course].add(pre)
            indegree[pre] += 1
        
        
        print(graph)
        print(indegree)

        topo = []
        q = deque([i for i,degree in enumerate(indegree) if degree == 0])
        print(q)
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return len(topo) == numCourses
