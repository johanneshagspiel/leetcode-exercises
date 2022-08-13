from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return root

        res = []

        def pre_order(node):
            if node:
                res.append(node)
                pre_order(node.left)
                pre_order(node.right)

        pre_order(root)
        N = len(res)

        for i in range(N-1):
            res[i].right = res[i+1]
            res[i].left = None

        res[N-1].right = None
        res[N-1].left = None

        return root

