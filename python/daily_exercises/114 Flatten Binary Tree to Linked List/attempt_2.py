from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        if not root:
            return root

        stack = []
        stack.append(root)
        dummy = TreeNode()
        prev = dummy

        while stack:
            node = stack.pop()

            prev.right = node
            prev.left = None
            prev = prev.right

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return dummy.right

