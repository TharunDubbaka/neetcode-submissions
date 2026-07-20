# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def buildpath(root,tar):
            path=[]
            while root:
                path.append(root)
                if root.val==tar:
                    #path.append(str(root.val))
                    return path
                elif root.val<tar:
                    root=root.right
                else:
                    root=root.left
            return path
        pa=buildpath(root,p.val)
        pb=buildpath(root,q.val)
        minlen=min(len(pa),len(pb))
        lca=0
        for i in range(minlen):
            if pa[i]==pb[i]:
                lca=pa[i]
        return lca


            
