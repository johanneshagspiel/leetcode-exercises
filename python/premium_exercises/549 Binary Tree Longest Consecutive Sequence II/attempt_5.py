from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:


        def longestPath(root):
            nonlocal max_val

            if not root:
                return (0, 0)

            inc = 1
            dec = 1

            if root.left:
                left_inc, left_dec = longestPath(root.left)
                if root.val == (root.left.val + 1):
                    inc += left_inc
                elif root.val == (root.left.val - 1):
                    dec += left_dec

            if root.right:
                right_inc, right_dec = longestPath(root.right)
                if root.val == (root.right.val + 1):
                    inc = max(inc, 1 + right_inc)
                elif root.val == (root.right.val - 1):
                    dec = max(dec, 1 + right_dec)

            max_val = max(max_val, inc + dec - 1)
            return inc, dec

        max_val = 0
        longestPath(root)
        return max_val
