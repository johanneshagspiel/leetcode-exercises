from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.result_array = []
        self.recursive_inordertraversal(root)

    def recursive_inordertraversal(self, root):

        if root:

            self.recursive_inordertraversal(root.left)
            self.result_array.append(root.val)
            self.recursive_inordertraversal(root.right)

        return
