from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = []
        seen = set()

        res = []

        stack.append(root)

        while stack:

            node = stack[-1]

            if (not node.left) or (node.left in seen):
                stack.pop()
                seen.add(node)
                res.append(node.val)

            if node.left and node.left not in seen:
                stack.append(node.left)

            elif node.right and node.right not in seen:
                stack.append(node.right)

        return res
