# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def buildstrings(root):
            if not root:
                return "None"
            return (str(root.val)+buildstrings(root.left)+buildstrings(root.right))
        sa=buildstrings(root)
        sb=buildstrings(subRoot)
        return sb in sa
        #print(sa)
        
        
            