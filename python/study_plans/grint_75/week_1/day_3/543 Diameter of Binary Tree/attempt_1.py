from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root:
            current_max = self.diameterOfBinaryTree_helper(root.left) + self.diameterOfBinaryTree_helper(root.right)
            return max(current_max, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        else:
            return 0

    def diameterOfBinaryTree_helper(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.right and root.left:
                return 1 + max(self.diameterOfBinaryTree_helper(root.right),
                               self.diameterOfBinaryTree_helper(root.left))
            elif root.right:
                return 1 + self.diameterOfBinaryTree_helper(root.right)
            elif root.left:
                return 1 + self.diameterOfBinaryTree_helper(root.left)
            else:
                return 1
        else:
            return 1
