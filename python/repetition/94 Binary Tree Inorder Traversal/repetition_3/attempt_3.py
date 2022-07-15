from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        result_list = []

        while stack or root:

            if root:
                stack.append(root)
                root = root.left

            else:
                node = stack.pop()
                result_list.append(node.val)
                root = node.right

        return result_list
