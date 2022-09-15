from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = []
        stack.append((root, 0))

        com_path_sum = 0

        while stack:
            node, path_sum = stack.pop()
            path_sum = path_sum * 10 + node.val

            if not node.left and not node.right:
                com_path_sum += path_sum

            else:
                if node.left:
                    stack.append((node.left, path_sum))
                if node.right:
                    stack.append((node.right, path_sum))

        return com_path_sum
