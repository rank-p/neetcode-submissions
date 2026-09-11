class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for (u,v) in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        seen = set()
        def dfs(n, seen):
            if n in seen:
                return
            seen.add(n)
            for nei in graph[n]:
                dfs(nei, seen)
        
        components = 0
        for node in range(n):
            if node not in seen:
                components += 1
                dfs(node, seen)
        
        return components
