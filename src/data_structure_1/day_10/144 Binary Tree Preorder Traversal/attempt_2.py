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

        if root:
            stack.append(root)

            while stack:
                current_node = stack.pop()
                result_list.append(current_node.val)

                if current_node.right:
                    stack.append(current_node.right)

                if current_node.left:
                    stack.append(current_node.left)

        return result_list