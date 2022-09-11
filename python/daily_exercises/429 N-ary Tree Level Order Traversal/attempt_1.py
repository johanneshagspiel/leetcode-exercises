import collections
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        res = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            level_length = len(queue)
            level_list = []

            for element in range(level_length):
                node = queue.popleft()
                level_list.append(node.val)

                for child in node.children:
                    queue.append(child)

            res.append(level_list)

        return res

