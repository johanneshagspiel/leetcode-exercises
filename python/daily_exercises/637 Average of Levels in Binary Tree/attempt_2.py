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

        res = []

        if not root:
            return res

        queue = collections.deque()
        queue.append(root)

        while queue:

            acc = 0
            n = 0

            queue_len = len(queue)

            for element in range(queue_len):
                node = queue.popleft()
                acc += node.val
                n += 1

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            temp = round(acc / n, 5)
            res.append(temp)

        return res

