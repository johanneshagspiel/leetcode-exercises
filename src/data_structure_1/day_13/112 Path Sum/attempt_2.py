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

        def path_sum_recursion(root, cum_sum):
            new_cum_sum = cum_sum + root.val

            if not root.left and not root.right:
                if new_cum_sum == targetSum:
                    return True
            else:
                if root.right and root.left:
                    return self.hasPathSum(root.right, new_cum_sum) or self.hasPathSum(root.left, new_cum_sum)
                elif root.right and not root.left:
                    return self.hasPathSum(root.right, new_cum_sum)
                elif not root.right and root.left:
                    return self.hasPathSum(root.left, new_cum_sum)
                else:
                    return False


        if not root:
            return False
        else:
            return path_sum_recursion(root, 0)

