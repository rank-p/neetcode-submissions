class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def search(r,c,i):
            # print(curr)
            if len(word) == i:
                return True
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if (r,c) in seen or board[r][c] != word[i]:
                return False

            seen.add((r,c))

            found = any(
                search(r+dr,c+dc,i+1)
                for dr,dc in ((0,1),(0,-1),(1,0),(-1,0))
            )
            
            seen.remove((r,c))
            return found
        
        for r in range(rows):
            for c in range(cols):
                if search(r,c,0):
                    return True
        
        return False
            
