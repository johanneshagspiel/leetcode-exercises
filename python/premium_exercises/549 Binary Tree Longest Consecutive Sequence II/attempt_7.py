from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        max_val = 0

        def rec(node):

            if not node:
                return 0, 0

            else:
                nonlocal max_val

                inc = 1
                dec = 1

                if node.left:
                    left_inc, left_dec = rec(node.left)

                    if node.left.val == node.val + 1:
                        inc = max(inc, left_inc + 1)

                    elif node.left.val == node.val - 1:
                        dec = max(dec, left_dec + 1)

                if node.right:
                    right_inc, right_dec = rec(node.right)

                    if node.right.val == node.val + 1:
                        inc = max(inc, right_inc + 1)

                    elif node.right.val == node.val - 1:
                        dec = max(dec, right_dec + 1)

                max_val = max(max_val, inc + dec - 1)
                return inc, dec

        rec(root)
        return max_val
