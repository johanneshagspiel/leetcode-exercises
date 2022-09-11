# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0

        def rec(node, prev_max_value):
            nonlocal good_nodes

            if node:
                if node.val >= prev_max_value:
                    good_nodes += 1
                    rec(node.left, node.val)
                    rec(node.right, node.val)
                else:
                    rec(node.left, prev_max_value)
                    rec(node.right, prev_max_value)

        rec(root, -float("inf"))
        return good_nodes
    