# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #for each node,abs(left height-right hieght)<=1
        if not root:
            return True
        self.res=True
        def maxDepth(root):
            if not root:
                return 0

            l = maxDepth(root.left)
            r = maxDepth(root.right)
            if abs(l-r)>1:
                self.res=False
            
            return 1 + max(l, r)
        maxDepth(root)
        return self.res
        
        