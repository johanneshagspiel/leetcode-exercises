# Definition for a Node.
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None
        else:

            queue = collections.deque()
            queue.append(root)

            while queue:
                level_length = len(queue)
                level_array = []
                for current_element in range(level_length):
                    level_array.append(queue.popleft())

                for current_index in range(level_length):
                    current_node = level_array[current_index]

                    if (current_index + 1) < level_length:
                        current_node.next = level_array[current_index + 1]
                    else:
                        current_node.next = None

                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)

            return root
