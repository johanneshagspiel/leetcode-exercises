from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None


        def rec(node):

            if not node:
                return False

            if node.val == 1:
                correct_left = rec(node.left)
                if not correct_left:
                    node.left = None

                correct_right = rec(node.right)
                if not correct_right:
                    node.right = None

                return True

            elif node.val == 0:
                correct_left = rec(node.left)
                if not correct_left:
                    node.left = None

                correct_right = rec(node.right)
                if not correct_right:
                    node.right = None

                if any([correct_left, correct_right]):
                    return True
                else:
                    return False

        correct_root = rec(root)
        if correct_root:
            return root
        else:
            return None
