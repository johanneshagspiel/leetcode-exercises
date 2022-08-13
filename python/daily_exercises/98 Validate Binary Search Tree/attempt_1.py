from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prev = -float("inf")

        def rec(root):

            if not root:
                return True

            if not rec(root.left):
                return False

            if root.val < self.prev:
                return False

            self.prev = root.val

            return rec(root.right)

        return rec(root)

