from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        else:
            if root.left:
                if root.left.val < root.val:
                    left_result = self.isValidBST(root.left)
                else:
                    left_result = False
            else:
                left_result = None

            if root.right:
                if root.right.val > root.val:
                    right_result = self.isValidBST(root.right)
                else:
                    right_result = False
            else:
                right_result = None

            if left_result != None and right_result != None:
                return (left_result and right_result)
            elif left_result:
                return left_result
            elif right_result:
                return right_result
            else:
                return True

