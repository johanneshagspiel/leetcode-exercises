import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        queue = collections.deque()
        queue.append(root)

        res = []
        mode = 1

        while queue:

            level = collections.deque()
            len_queue = len(queue)

            for element in range(len_queue):
                node = queue.popleft()

                if mode == 0:
                    level.appendleft(node.val)
                elif mode == 1:
                    level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            if mode == 1:
                mode = 0
            else:
                mode = 1

            res.append(level)

        return res
