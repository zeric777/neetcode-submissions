# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        if not root:
            return []
        r=[]
        queue=deque()
        queue.append(root)
        
        while queue:
            l=[]
            le=len(queue)
            for i in range(le):
                e=queue.popleft()
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
                l.append(e.val)
            r.append(l)
        return r

