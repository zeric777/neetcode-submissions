# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #dfs
        if not root:
            return []
        q=deque([root])
        r=[]
        while q:
            l=len(q)
            k=1
            for i in range(len(q)):
                e=q.popleft()
                if k==1:
                    r.append(e.val)
                k+=1
                if e.right:
                    q.append(e.right)
                if e.left:
                    q.append(e.left)
                
        return r