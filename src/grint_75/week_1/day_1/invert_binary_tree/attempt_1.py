from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            if root.left and root.right:
                return TreeNode(val=root.val, left=self.invertTree(root.right), right=self.invertTree(root.left))
            elif root.left:
                return TreeNode(val=root.val, right=self.invertTree(root.left))
            elif root.right:
                return TreeNode(val=root.val, left=self.invertTree(root.right))
            else:
                return TreeNode(val=root.val)
        else:
            return None
