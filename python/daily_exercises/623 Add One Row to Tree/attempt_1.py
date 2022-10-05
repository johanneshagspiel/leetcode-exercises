import collections
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if not root:
            return root

        elif depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        level = 1
        queue = collections.deque()
        queue.append(root)

        while queue:

            queue_len = len(queue)

            for _ in range(queue_len):

                node = queue.popleft()

                if level == (depth - 1):

                    if node.left:
                        new_left_node = TreeNode(val)
                        prev_left = node.left

                        node.left = new_left_node
                        new_left_node.left = prev_left
                    else:
                        new_left_node = TreeNode(val)
                        node.left = new_left_node

                    if node.right:
                        new_right_node = TreeNode(val)
                        prev_right = node.right

                        node.right = new_right_node
                        new_right_node.right = prev_right
                    else:
                        new_right_node = TreeNode(val)
                        node.right = new_right_node

                else:
                    if node.right:
                        queue.append(node.right)

                    if node.left:
                        queue.append(node.left)

            level += 1

        return root
