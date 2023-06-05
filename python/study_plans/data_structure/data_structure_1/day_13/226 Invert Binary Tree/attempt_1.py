from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert_helper(root):
            if root:
                right = self.invertTree(root.right)
                left = self.invertTree(root.left)
                root.left = right
                root.right = left

        invert_helper(root)
        return root


