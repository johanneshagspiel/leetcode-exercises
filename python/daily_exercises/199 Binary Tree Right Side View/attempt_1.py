from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right_value_list = []
        left_value_list = []

        def check_right(node):
            while node:
                right_value_list.append(node.val)
                check_right(node.right)

        def check_left(node):
            while node:
                left_value_list.append(node.val)
                check_right(node.left)


        check_right(root)
        check_left(root)

        r_len = len(right_value_list)
        l_len = len(left_value_list)

        if r_len > l_len:
            return right_value_list
        else:
            combined_list = right_value_list + left_value_list[r_len:]
            return combined_list
