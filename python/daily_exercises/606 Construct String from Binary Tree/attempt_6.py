from typing import Optional# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        res = ""

        stack = []
        stack.append(root)

        seen = set()

        while stack:

            top_node = stack[-1]

            if top_node in seen:
                stack.pop()
                res += ")"

            else:
                res += "(" + str(top_node.val)
                seen.add(top_node)

            if top_node.left and top_node.right:
                if top_node.left not in seen:
                    stack.append(top_node.right)
                if top_node.right not in seen:
                    stack.append(top_node.left)

            elif top_node.left and not top_node.right:
                if top_node.left not in seen:
                    stack.append(top_node.left)

            elif not top_node.left and top_node.right:
                if top_node.right not in seen:
                    res += "()"
                    stack.append(top_node.right)

        return res[1:-1]
