from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = [(root, 1)]
        depth = 0

        if root:

            while stack:
                current_node, current_depth = stack.pop()

                if current_node:
                    if current_depth > depth:
                        depth = current_depth

                    current_depth += 1

                    stack.append((current_node.left, current_depth))
                    stack.append((current_node.right, current_depth))


        return depth
