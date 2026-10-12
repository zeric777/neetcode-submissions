# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        d=0
        while q:
            for i in range(len(q)):
                e=q.popleft()
                if e.right:
                    q.append(e.right)
                if e.left:
                    q.append(e.left)
            d+=1
        return d