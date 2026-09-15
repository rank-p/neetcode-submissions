class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        
        def dfs(r,c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return
            if grid[r][c] == "0":
                return
            if (r,c) in seen:
                return
            seen.add((r,c))
            for dr,dc in ((0,1), (0,-1), (1,0), (-1,0)):
                dfs(r+dr, c+dc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and ((r,c)) not in seen:
                    islands += 1
                    dfs(r,c)
        
        return islands