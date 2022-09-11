from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def rec_inorder(node):

            if node:
                rec_inorder(node.left)
                res.append(node.val)
                rec_inorder(node.right)

        rec_inorder(root)
        return res


