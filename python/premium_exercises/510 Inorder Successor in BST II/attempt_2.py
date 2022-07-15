from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        if not node:
            return node

        start_node = node

        while node.parent:
            node = node.parent

            if node.val > start_node.val:
                return node

        return None

    # [2, 1, 3]
    # 1
    # [5, 3, 6, 2, 4, null, null, 1]
    # 6