from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result_list = []

        def rec(node):
            if node:
                result_list.append(node.val)
                rec(node.left)
                rec(node.right)

        N = len(result_list)

        for position in range(2, N):
            if result_list[position] <= result_list[position-1]:
                return False

        return True
