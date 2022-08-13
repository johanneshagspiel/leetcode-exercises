import collections
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result_dic = {}

        queue = collections.deque()
        queue.append((root, 0))

        min_level = 0
        max_level = 0

        while queue:

            height = len(queue)

            for num in range(height):

                node, level = queue.popleft()

                if level not in result_dic:
                    result_dic[level] = []
                result_dic[level].append(node.val)

                if node.left:
                    min_level = min(min_level, level -1)
                    queue.append((node.left, level-1))

                if node.right:
                    max_level = max(max_level, level+1)
                    queue.append((node.right, level+1))

        res = []

        for index in range(min_level, max_level+1):
            res.append(result_dic[index])

        return res