from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def rec_val(left_tree, right_tree):
            if left_tree and not right_tree:
                return False

            elif not left_tree and right_tree:
                return False

            elif not left_tree and not right_tree:
                return True

            else:
                if left_tree.val != right_tree.val:
                    return False
                else:
                    return True and rec_val(left_tree.left, right_tree.right) and rec_val(left_tree.right, right_tree.left)

        return rec_val(root.left, root.right)
    