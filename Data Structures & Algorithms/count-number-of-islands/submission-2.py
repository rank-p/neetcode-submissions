class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        v = set()
        def inBounds(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def dfs(r,c,v):
            if (r,c) in v or not inBounds(r,c) or grid[r][c] == "0":
                return
            
            v.add((r,c))
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                dfs(r+dr, c+dc,v)

        islands = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "1" and (r,c) not in v:
                    islands += 1
                    dfs(r,c,v)
        return islands
