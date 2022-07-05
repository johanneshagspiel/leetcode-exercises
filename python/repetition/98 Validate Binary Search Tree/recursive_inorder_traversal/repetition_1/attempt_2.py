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

            left_value = self.isValidBST(root.left)

            if root.left:
                current_left = root.left.val < root.val
            else:
                current_left = True

            if root.right:
                current_right = root.right.val > root.val
            else:
                current_right = True

            right_value = self.isValidBST(root.right)

            if current_left and current_right:
                return left_value and right_value
            else:
                return False
