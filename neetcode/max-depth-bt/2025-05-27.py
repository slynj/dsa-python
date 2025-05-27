# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth = self.maxDepthHelper(root, 0)

        return depth
    

    def maxDepthHelper(self, root, depth):
        if root is None:
            return depth
        
        maxD = max(self.maxDepthHelper(root.left, depth + 1), self.maxDepthHelper(root.right, depth + 1))

        return maxD


