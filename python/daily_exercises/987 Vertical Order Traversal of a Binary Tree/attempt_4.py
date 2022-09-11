import collections
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

        stack = []
        stack.append((root, 0, 0))
        column_dic = {}

        min_col = 0
        max_col = 0

        while stack:

            node, column, row = stack.pop()

            if column not in column_dic:
                column_dic[column] = []
            column_dic[column].append((row, node.val))

            min_col = min(column, min_col)
            max_col = max(column, max_col)

            if node.left:
                stack.append((node.left, column - 1, row + 1))
            if node.right:
                stack.append((node.right, column + 1, row + 1))

        res = []

        for column in range(min_col, max_col + 1):
            value_list = column_dic[column]
            value_list.sort()
            res.append([x[1] for x in value_list])

        return res

