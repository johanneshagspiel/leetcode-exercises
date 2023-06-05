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

        def in_order_check(root):

            if not root:
                return True
            if not in_order_check(root.left):
                return False
            if root.val <= self.previous:
                return False
            self.previous = root.val
            return in_order_check(root.right)

        self.previous = -math.inf
        return in_order_check(root)
