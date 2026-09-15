# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []

        def traverse(node):
            if node is None:
                tokens.append("N")
                return
            
            tokens.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return "#".join(tokens)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split("#"))

        def build():
            value = next(tokens)
            if value == "N":
                return None
            
            node = TreeNode(int(value))
            node.left = build()
            node.right = build()
            return node
        return build()

            




