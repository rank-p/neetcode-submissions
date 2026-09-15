class PrefixNode:
        def __init__(self, val=None, is_word=False):
            self.val = val
            self.children = {}
            self.is_word = is_word

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixNode(c)
            node = node.children[c]
        node.is_word = True

    def _find(self, word: str) -> PrefixNode:
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        