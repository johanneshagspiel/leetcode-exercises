from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = []
        stack.append((root, -math.inf, math.inf))

        while stack:
            node, low, high = stack.pop()
            if node:

                if low < node.val < high:
                    stack.append((node.left, low, node.val))
                    stack.append((node.right, node.val, high))
                else:
                    return False

        return True
