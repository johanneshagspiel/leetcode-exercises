from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        res = ""

        def rec(node):

            nonlocal res

            res += str(node.val)

            if node.left and node.right:
                res += "("
                rec(node.left)
                res += ")"

                res += "("
                rec(node.right)
                res += ")"

            elif node.left and not node.right:
                res += "("
                rec(node.left)
                res += ")"

            elif not node.left and node.right:
                res += "()("
                rec(node.right)
                res += ")"

        if root:
            rec(root)

        return res
