from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        value_list = []

        def rec(node):

            if node:
                rec(node.left)
                value_list.append(node.val)
                rec(node.right)

        rec(root)

        left = 0
        right = len(value_list) - 1

        while left < right:
            comb = value_list[left] + value_list[right]

            if comb == k:
                return True

            elif comb < k:
                left += 1

            else:
                right -= 1

        return False
