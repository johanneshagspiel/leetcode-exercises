from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        if node.right:

            node = node.right
            while node.left:
                node = node.left

            return node

        else:
            previous_node = node

            while node.parent:

                node = node.parent
                if previous_node == node.left:
                    return previous_node
                else:
                    previous_node = node

            return None
