from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result_list = []
        stack = [root]

        while stack:

            current_node = stack.pop()

            result_list.append(current_node.val)
            stack.append(current_node.left)
            stack.append(current_node.right)

        return result_list[::-1]