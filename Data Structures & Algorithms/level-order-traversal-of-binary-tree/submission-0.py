# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                c = q.popleft()
                level.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            levels.append(level)

        return levels