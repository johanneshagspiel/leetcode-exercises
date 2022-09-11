from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def rec(node):

            if not node:
                return False

            else:

                contain_one = node.val == 1

                left_contain_one = False
                if node.left:
                    left_contain_one = rec(node.left)

                    if not left_contain_one:
                        node.left = None

                right_contain_one = False
                if node.right:
                    right_contain_one = rec(node.right)

                    if not right_contain_one:
                        node.right = None

                return any([contain_one, left_contain_one, right_contain_one])

        root_one = rec(root)
        if root_one:
            return root
        else:
            return None

