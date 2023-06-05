from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result_list = []

        def rec(node):
            if node:
                rec(node.left)
                rec(node.right)
                result_list.append(node.val)

        rec(root)
        return result_list
