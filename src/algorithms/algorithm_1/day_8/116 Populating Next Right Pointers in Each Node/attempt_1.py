import collections
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        queue = collections.deque([root])

        while queue:

            new_queue = collections.deque()
            current_node = queue.popleft()

            if current_node.left:
                new_queue.append(current_node.left)
            if current_node.right:
                new_queue.append(current_node.right)

            queue_length = len(queue)
            for vertex in range(queue_length):
                next_node = queue.popleft()
                current_node.right = next_node
                current_node = next_node

                if current_node.left:
                    new_queue.append(current_node.left)
                if current_node.right:
                    new_queue.append(current_node.right)

            current_node.right = None

            queue = new_queue

        return root
