import collections
from typing import Optional


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

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:

            queue_length = len(queue)
            acc = 0
            n = 0

            for element in range(queue_length):
                node = queue.popleft()
                acc += node.val
                n += 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average = acc / n
            res.append(average)

        return res
