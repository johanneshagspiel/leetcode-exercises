from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        palindrom_count = 0

        def rec(node, path):

            nonlocal palindrom_count

            if node:
                path ^= 1 << node.val

                if not node.left and not node.right:
                    if (path) & (path - 1) == 0:
                        palindrom_count += 1
                else:
                    rec(node.left, path)
                    rec(node.right, path)

        rec(root, 0)
        return palindrom_count
