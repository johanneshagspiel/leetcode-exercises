import collections
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []

        queue = collections.deque()
        queue.append(root)
        mode = 0

        while queue:

            level_queue = collections.deque()
            level_len = len(queue)

            for position in range(level_len):
                node = queue.popleft()

                if mode == 0:
                    level_queue.append(node.val)
                else:
                    level_queue.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if mode == 0:
                mode = 1
            else:
                mode = 0

            res.append(level_queue)

        return res
