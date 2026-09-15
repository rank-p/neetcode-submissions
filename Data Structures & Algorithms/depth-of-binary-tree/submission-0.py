# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]
        
        def search(node, depth):
            if not node:
                return
            depth += 1
            max_depth[0] = max(depth, max_depth[0])
            search(node.left, depth)
            search(node.right, depth)
        
        search(root, 0)
        return max_depth[0]
        