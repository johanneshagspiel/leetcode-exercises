
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.diameterOfBinaryTree_rec(root)
        return self.diameter

    def diameterOfBinaryTree_rec(self, root):
        if not root:
            return 0

        left_longest_path = self.diameterOfBinaryTree_rec(root.left)
        right_longest_path = self.diameterOfBinaryTree_rec(root.right)

        self.diameter = max(self.diameter, left_longest_path + right_longest_path)

        return max(left_longest_path, right_longest_path) + 1