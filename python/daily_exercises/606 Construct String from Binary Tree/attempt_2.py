from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        stack = []
        stack.append(root)

        res = ""
        seen = set()

        while stack:

            node= stack[-1]

            if node not in seen:
                res += "(" + str(node.val)
                seen.add(node)
            else:
                stack.pop()
                res += ")"

            if node.left and node.right:
                if node.left not in seen:
                    stack.append(node.right)
                if node.right not in seen:
                    stack.append(node.left)

            elif node.left and not node.right:
                if node.left not in seen:
                    stack.append(node.left)

            elif not node.left and node.right:
                if node.right not in seen:
                    res += "()"
                    stack.append(node.right)

        return res[1:-1]

