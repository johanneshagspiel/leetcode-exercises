from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result_list = []
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node:
                result_list.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return result_list
