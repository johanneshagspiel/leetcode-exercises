from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def rec(left, right):

            if not left and not right:
                return True
            elif not left and right:
                return False
            elif left and not right:
                return False
            else:

                if left.val == right.val:
                    left_left = left.left
                    left_right = left.right

                    right_left = right.left
                    right_right = right.right

                    return rec(left_left, right_right) and rec(left_right, right_left)

                else:
                    return False


        if not root:
            return True
        else:
            return rec(root.left, root.right)
