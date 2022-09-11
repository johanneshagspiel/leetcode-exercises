import collections
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        stack = []
        stack.append((root, 0, 0))

        result_list = []

        while stack:
            node, column, row = stack.pop()

            result_list.append((column, row, node.val))

            if node.left:
                stack.append((node.left, column - 1, row + 1))

            if node.right:
                stack.append((node.right, column + 1, row + 1))

        result_list.sort()

        current_column = result_list[0][0]

        res = []
        column_list = []
        for column, row, value in result_list:
            if column == current_column:
                column_list.append(value)
            else:
                res.append(column_list)
                current_column = column
                column_list = []
                column_list.append(value)
        res.append(column_list)
        return res



