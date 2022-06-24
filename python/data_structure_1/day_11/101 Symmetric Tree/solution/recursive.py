import collections
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        else:
            return self.recursive_symmetry(root.left, root.right)

    def recursive_symmetry(self, left_node, right_node):

        if left_node and not right_node:
            return False
        elif not left_node and right_node:
            return False
        elif not left_node and not right_node:
            return True
        else:
            if left_node.val == right_node.val:
                return self.recursive_symmetry(left_node.left, right_node.right) & self.recursive_symmetry(left_node.right, right_node.left)
            else:
                return False
