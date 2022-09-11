from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        max_len = 0


        def rec(node):

            nonlocal max_len

            if not node:
                return [0, 0]

            else:

                inc = dcr = 1

                if node.left:
                    left_inc, left_dec = rec(node.left)

                    if node.left.val + 1 == node.val:
                        dcr = max(dcr, left_dec + 1)
                    elif node.left.val - 1 == node.val:
                        inc = max(inc, left_inc + 1)

                if node.right:
                    right_inc, right_dec = rec(node.right)

                    if node.right.val + 1 == node.val:
                        dcr = max(dcr, right_dec + 1)
                    elif node.right.val - 1 == node.val:
                        inc = max(inc, right_dec + 1)

                max_len = max(max_len, inc + dcr - 1)
                return inc, dcr

        rec(root)
        return max_len
