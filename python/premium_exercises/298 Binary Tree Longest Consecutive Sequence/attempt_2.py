from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = []
        stack.append((root, float("inf"), 1))

        max_path = 1

        while stack:
            node, previous_value, path_len = stack.pop()

            if previous_value == node.val - 1:

                max_path = max(max_path, path_len + 1)

                if node.left:
                    stack.append((node.left, node.val, path_len + 1))
                if node.right:
                    stack.append((node.right, node.val, path_len + 1))

            else:

                if node.left:
                    stack.append((node.left, node.val, 1))
                if node.right:
                    stack.append((node.right, node.val, 1))

        return max_path
