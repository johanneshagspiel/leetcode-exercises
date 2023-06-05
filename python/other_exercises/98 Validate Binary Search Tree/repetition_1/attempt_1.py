from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.value_list = []

        def rec_inorder(node):

            if node:
                rec_inorder(node.left)
                self.value_list.append(node.val)
                rec_inorder(node.right)


        rec_inorder(root)

        N = len(self.value_list)
        print(self.value_list)

        for position in range(1, N):
            if self.value_list[position-1] >= self.value_list[position]:
                return False

        return True
