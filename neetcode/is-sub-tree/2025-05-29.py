# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        # if not root and not subRoot:
        #     return True
        # elif not root or not subRoot:
        #     return False
        
        # if root.val == subRoot.val:
        #     return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right) or (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        # else:
        #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    



