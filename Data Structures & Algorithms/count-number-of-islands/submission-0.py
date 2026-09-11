class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        v = set()
        def inBounds(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def dfs(r,c,v):
            if (r,c) in v or not inBounds(r,c) or grid[r][c] == "0":
                return
            
            v.add((r,c))
            dfs(r+1,c,v)
            dfs(r-1,c,v)
            dfs(r,c+1,v)
            dfs(r,c-1,v)
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in v:
                    continue
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c,v)
        return islands
