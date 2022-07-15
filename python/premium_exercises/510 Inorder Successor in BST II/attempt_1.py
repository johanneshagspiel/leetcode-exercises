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

        root = node

        node_list = []

        def rec(node):
            if node:
                rec(node.left)
                node_list.append((node.val, node))
                rec(node.right)

        rec(root)

        found_index = -1
        index = 0
        for value, node in node_list:
            if value == start_node.val:
                found_index = index
                break
            index += 1

        if found_index == len(node_list):
            return None
        else:
            return node_list[found_index][1]


