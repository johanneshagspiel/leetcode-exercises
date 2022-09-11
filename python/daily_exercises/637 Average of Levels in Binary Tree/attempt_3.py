import collections
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        acc = []
        n = []

        stack = []
        stack.append((root, 1))

        while stack:
            node, level = stack.pop()

            if level > len(acc):
                acc.append([])
                n.append(0)

            acc[level-1].append(node.val)
            n[level-1] += 1

            if node.left:
                stack.append((node.left, level + 1))

            if node.right:
                stack.append((node.right,level + 1))

        res = []

        for level in range(len(acc)):
            level_sum = sum(acc[level])
            temp = round(level_sum / n[level], 5)
            res.append(temp)

        return res
            