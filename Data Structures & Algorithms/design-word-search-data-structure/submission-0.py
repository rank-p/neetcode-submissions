class PrefixNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixNode(c)
            node = node.children[c]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        def _search(node, word):
            for i,c in enumerate(word):
                if c == ".":
                    return any(
                        _search(children, word[i+1:]) for children in node.children.values()
                    )
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.is_word
       
        return _search(self.root, word)
