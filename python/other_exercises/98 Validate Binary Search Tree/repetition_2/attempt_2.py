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

        def inorder(node):

            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.prev > node.val:
                return False
            self.prev = node.val

            return inorder(node.right)

        inorder(root)
