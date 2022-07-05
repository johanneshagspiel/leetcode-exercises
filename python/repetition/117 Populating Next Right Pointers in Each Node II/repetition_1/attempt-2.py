import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root == None:
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:
            current_breadth = len(queue)

            previous_element = queue.popleft()

            if previous_element.left:
                queue.append(previous_element.left)
            if previous_element.right:
                queue.append(previous_element.right)

            for element in range(current_breadth - 1):
                current_node = queue.popleft()

                previous_element.next = current_node
                previous_element = current_node

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

        return root