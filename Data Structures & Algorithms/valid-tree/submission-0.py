class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for (u,v) in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        print(graph)
        seen = set()
        def dfs(n,seen):
            if n in seen:
                return
            seen.add(n)
            for nei in graph[n]:
                dfs(nei,seen)
        
        dfs(0,seen)
        return len(seen) == n and len(edges) == (n-1)
