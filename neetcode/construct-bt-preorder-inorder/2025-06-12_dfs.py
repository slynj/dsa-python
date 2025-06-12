# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = { val : i for i, val in enumerate(inorder)}

        self.idx = 0

        def dfs(l, r):
            if l > r :
                return None
            
            rootVal = preorder[self.idx]
            self.idx += 1

            root = TreeNode(rootVal)
            rootIdx = inorderIdx[rootVal]

            root.left = dfs(l, rootIdx - 1)
            root.right = dfs(rootIdx + 1, r)
            
            return root
        
        return dfs(0, len(inorder)-1)









