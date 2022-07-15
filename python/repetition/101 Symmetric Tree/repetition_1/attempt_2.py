from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        stack.append((root.left, root.right))

        while stack:
            left_node, right_node = stack.pop()

            if left_node and not right_node:
                return False
            elif not left_node and right_node:
                return False
            elif left_node and right_node:

                if left_node.val != right_node.val:
                    return False
                else:
                    stack.append((left_node.left, right_node.right))
                    stack.append((left_node.right, right_node.left))

        return True
