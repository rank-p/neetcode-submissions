class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def search(r,c,curr, seen):
            # print(curr)
            if curr == word:
                return True
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if len(curr) > len(word):
                return False
            if (r,c) in seen:
                return False
            seen.add((r,c))
            curr += board[r][c]

            any_true = False
            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                any_true = any_true or search(r+dr,c+dc,curr,seen)
            
            seen.remove((r,c))
            return any_true
        
        for r in range(rows):
            for c in range(cols):
                if search(r,c,"",seen):
                    return True
        
        return False
            
