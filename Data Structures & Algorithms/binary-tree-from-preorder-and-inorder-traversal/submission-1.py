# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {val: i for i,val in enumerate(inorder)}
        values = iter(preorder)

        def build(left, right):
            if left > right:
                return None

            val = next(values)
            mid = positions[val]

            node = TreeNode(val)
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)
            return node

        return build(0, len(inorder)-1)

        