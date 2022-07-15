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

        self.found = False
        self.next_found = False
        self.next_node = None

        def rec_inorder(node):

            if node:
                rec_inorder(node.left)

                if node == start_node:
                    self.found = True
                elif self.found and not self.next_found:
                    self.next_node = node
                    self.next_found = True

                rec_inorder(node.right)

        rec_inorder(node)
        return self.next_node


