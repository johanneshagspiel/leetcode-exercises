# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = []
        stack.append((root, -float("inf")))

        res = 0

        while stack:
            current_node, prev_max_value = stack.pop()

            if current_node.val >= prev_max_value:
                res += 1

            new_max_value = max(prev_max_value, current_node.val)

            if current_node.left:
                stack.append((current_node.left, new_max_value))
            if current_node.right:
                stack.append((current_node.right, new_max_value))

        return res
