import math
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.previous = -math.inf

        def inorder(root):

            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.previous:
                return False
            self.previous = root.val
            return inorder(root.right)

        return inorder(root)
