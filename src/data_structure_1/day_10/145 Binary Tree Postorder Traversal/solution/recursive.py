from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result_list = []
        self.recursive_postorder_traversal(root)

    def recursive_postorder_traversal(self, root):

        if root:
            self.recursive_postorder_traversal(root.left)
            self.recursive_postorder_traversal(root.right)
            self.result_list.append(root.val)

        return