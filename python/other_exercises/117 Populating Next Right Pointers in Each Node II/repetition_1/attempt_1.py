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

        queue = collections.deque()
        queue.append(root)

        while queue:
            current_level_length = len(queue)
            previous_element = queue.popleft()

            for element in range(current_level_length - 1):
                node = queue.popleft()

                previous_element.next = node
                previous_element = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            previous_element.next = None
            if previous_element.left:
                queue.append(previous_element.left)

            if previous_element.right:
                queue.append(previous_element.right)

        return root