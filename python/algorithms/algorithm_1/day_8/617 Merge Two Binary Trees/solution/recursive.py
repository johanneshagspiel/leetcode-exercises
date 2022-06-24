from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 and root2:
            combined_val = root1.val + root2.val
            left_tree = self.mergeTrees(root1.left, root2.left)
            right_tree = self.mergeTrees(root1.right, root2.right)

            root1.val = combined_val
            root1.left = left_tree
            root1.right = right_tree
            return root1

        elif root1:
            return root1

        elif root2:
            return root2

        else:
            return None