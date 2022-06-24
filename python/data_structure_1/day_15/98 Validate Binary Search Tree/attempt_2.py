import math
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        else:
            stack = []
            stack.append((root, -math.inf, math.inf))

            while stack:
                current_node, lower_limit, upper_limit = stack.pop()

                if current_node.val <= lower_limit or current_node.val >= upper_limit:
                    return False
                else:
                    if current_node.right:
                        stack.append((current_node.right, current_node.val, upper_limit))
                    if current_node.left:
                        stack.append((current_node.left, lower_limit, current_node.val))

            return True