import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None

        result_list = []
        queue = collections.deque()
        queue.append(root)

        while queue:

            level_list = []
            level = len(queue)

            for element in range(level):
                node = queue.popleft()
                if node:
                    level_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if len(level_list) > 0:
                result_list.append(level_list)

        return result_list
