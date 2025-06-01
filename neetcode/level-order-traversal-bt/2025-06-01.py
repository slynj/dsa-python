# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrderHelper(root, 0, [])
        
    def levelOrderHelper(self, root, lvl, lst):
        if not root:
            return lst

        if len(lst) < lvl+1:
            lst.append([])

        lst[lvl].append(root.val)

        self.levelOrderHelper(root.left, lvl+1, lst)
        self.levelOrderHelper(root.right, lvl+1, lst)

        return lst


