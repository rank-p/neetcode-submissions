class PrefixNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = PrefixNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixNode(c)
            node = node.children[c]
        node.is_word = True
    
    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
    
    def contains(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        seen = set()
        res = []

        # build trie
        for w in words:
            trie.insert(w)


        def traverse_grid(r,c,s):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if (r,c) in seen:
                return
            seen.add((r,c))
            s += board[r][c]
            node = trie.find(s)
            if not node:
                seen.remove((r,c))
                return
            else:
                if node.is_word:
                    res.append(s)
                    node.is_word = False
            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                traverse_grid(r+dr,c+dc,s)
            seen.remove((r,c))
            
        # build trie
        for r in range(rows):
            for c in range(cols):
                traverse_grid(r,c,"")
        
        return res

                






        