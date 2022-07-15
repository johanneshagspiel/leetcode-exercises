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
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:

            elements = len(queue)

            for element in range(elements):
                node = queue.popleft()
                
                if element < elements -2:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
