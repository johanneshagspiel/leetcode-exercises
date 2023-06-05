from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        number_list = []

        def get_value(root: Optional[TreeNode]):
            if not root:
                return

            else:
                get_value(root.left)
                number_list.append(root.val)
                get_value(root.right)

        get_value(root)

        if len(number_list) == 0:
            return True

        else:
            n = len(number_list)

            for index in range(1, n):
                if number_list[index] <= number_list[index - 1]:
                    return False

            return True