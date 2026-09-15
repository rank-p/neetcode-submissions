class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        def dfs(node, seen):
            if node in seen:
                return
            seen.add(node)
            for nei in graph[node]:
                dfs(nei,seen)
        
        comp = 0
        for node in range(n):
            if node not in seen:
                comp += 1
                dfs(node, seen)
        
        return comp