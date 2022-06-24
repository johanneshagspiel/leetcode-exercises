from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            root = TreeNode(val=val)
        else:
            self.recursive_insert(root, val)

        return root

    def recursive_insert(self, root, val):

        if val > root.val:
            if root.right:
                self.recursive_insert(root.right, val)
            else:
                root.right = TreeNode(val=val)
        else:
            if root.left:
                self.recursive_insert(root.left, val)
            else:
                root.left = TreeNode(val=val)