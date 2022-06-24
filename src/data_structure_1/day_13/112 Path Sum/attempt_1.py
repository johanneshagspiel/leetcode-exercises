import collections
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        else:
            stack = []
            stack.append((root, 0))

            while stack:
                current_node, cum_sum = stack.pop()
                path_sum = current_node.val + cum_sum

                if not current_node.right and not current_node.left:
                    if path_sum == targetSum:
                        return True
                else:
                    if current_node.left:
                        stack.append((current_node.left, path_sum))
                    if current_node.right:
                        stack.append((current_node.right, path_sum))

            return False
