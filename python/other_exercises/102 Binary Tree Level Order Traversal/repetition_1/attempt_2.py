from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None

        value_list = []

        def rec(node, level):

            if node:
                if level > len(value_list):
                    value_list.append([])

                value_list[level].append(node.val)
                rec(node.left, level+1)
                rec(node.right, level+1)

        rec(root, 1)
        return value_list
            