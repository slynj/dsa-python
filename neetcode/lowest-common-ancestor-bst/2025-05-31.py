# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        print(self.bst(root.left, p))
        print(self.bst(root.left, q))
        
        if self.bst(root.left, p) and self.bst(root.left, q):
            nexRoot = self.lowestCommonAncestor(root.left, p, q)
            if root.val < nexRoot.val:
                ancestor = root.val
            else:
                ancestor = nexRoot
            
        elif self.bst(root.right, p) and self.bst(root.right, q):
            nexRoot = self.lowestCommonAncestor(root.right, p, q)
            if root.val > nexRoot.val:
                ancestor = root.val
            else:
                ancestor = nexRoot
        else:
            ancestor = root
            
        return ancestor


    def bst(self, root, node):
        if not node:
            return True
        if not root:
            return False

        print(root.val)
        print(node.val)

        if node.val < root.val:
            return self.bst(root.left, node)
        elif node.val > root.val:
            return self.bst(root.right, node)
        elif root.val == node.val:
            return True
        

