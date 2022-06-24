from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 == None:
            return root2

        if root2 == None:
            return root1

        stack = [(root1, root2)]

        while stack:
            temp_root1, temp_root_2 = stack.pop()

            if (not temp_root1 or not temp_root_2):
                continue

            temp_root1.val += temp_root_2.val

            if (not temp_root1.left and temp_root_2.left):
                temp_root1.left = temp_root_2.left
            else:
                stack.append((temp_root1.left, temp_root_2.left))

            if (not temp_root1.right and temp_root_2.right):
                temp_root1.right = temp_root_2.right
            else:
                stack.append((temp_root1.right, temp_root_2.right))

        return root1
