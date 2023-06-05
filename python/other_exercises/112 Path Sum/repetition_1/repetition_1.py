from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        stack = []
        stack.append((root, 0))

        while stack:
            node, cur_sum = stack.pop()

            if node.left:
                stack.append((node.left, cur_sum + node.val))

            if node.right:
                stack.append((node.right, cur_sum + node.val))

            if not node.left and not node.right:
                total = cur_sum + node.val
                if total == targetSum:
                    return True

        return False
