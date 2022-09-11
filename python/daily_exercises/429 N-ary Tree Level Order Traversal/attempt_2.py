"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        res = []

        queue = collections.deque()
        queue.append(root)

        while queue:

            level = []

            for element in range(len(queue)):

                node = queue.popleft()

                if node:
                    level.append(node.val)

                    for child in node.children:
                        if child:
                            queue.append(child)

            if len(level) > 0:
                res.append(level)

        return res
