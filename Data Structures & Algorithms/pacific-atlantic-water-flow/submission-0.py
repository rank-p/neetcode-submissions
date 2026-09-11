class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, prev, ocean):
            if not (0 <= r < len(heights) and 0 <= c < len(heights[r])):
                return
            if (r,c) in ocean:
                return
            val = heights[r][c]            
            if val < prev:
                return
            
            ocean.add((r,c))
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                dfs(r+dr, c+dc, val, ocean)

        for r in range(rows):
            dfs(r,0,heights[r][0],pac)
            dfs(r,cols-1,heights[r][cols-1],atl)
        
        for c in range(cols):
            dfs(0,c,heights[0][c],pac)
            dfs(rows-1,c,heights[rows-1][c],atl)

        return [[r,c] for r,c in pac & atl]