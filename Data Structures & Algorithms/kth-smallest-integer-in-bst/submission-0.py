# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def preorder(root,k):
            if not root:
                return None

            preorder(root.left,k-1)
            res.append(root.val)
            preorder(root.right,k-1)
            return res
        r=preorder(root,k)
        return r[k-1]
        
            