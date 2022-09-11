from typing import List, Optional
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

        tuple_list = []

        stack = []
        stack.append((root, 0, 0))

        while stack:

            node, column, row = stack.pop()

            tuple_list.append((column, row, node.val))

            if node.left:
                stack.append((node.left, column - 1, row + 1))

            if node.right:
                stack.append((node.right, column + 1, row + 1))

        tuple_list.sort()

        res = []

        current_column = tuple_list[0][0]
        column_list = [tuple_list[0][2]]

        for column, row, value in tuple_list[1:]:
            if column != current_column:
                res.append(column_list)

                current_column = column
                column_list = []

            column_list.append(value)

        res.append(column_list)

        return res

