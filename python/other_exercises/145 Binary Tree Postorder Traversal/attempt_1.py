from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        value_list = []

        def rec(node):
            if node:
                rec(node.left)
                rec(node.right)
                value_list.append(node.val)

        rec(root)
        return value_list
    