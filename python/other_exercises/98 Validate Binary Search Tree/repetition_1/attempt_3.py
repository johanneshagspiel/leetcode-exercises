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

        self.prev = -math.inf

        def rec_inorder(node):

            if not node:
                return True

            if not self.rec_inorder(node.left):
                return False

            if self.prev >= node.val:
                return False

            self.prev = node.val

            return rec_inorder(node.right)

        return rec_inorder(root)