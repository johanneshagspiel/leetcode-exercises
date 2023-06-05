import collections
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        value_list = []
        queue = collections.deque()
        queue.append(root)
        level = 0

        while queue:

            queue_len = len(queue)
            value_list.append([])

            for element in range(queue_len):
                node = queue.popleft()
                value_list[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return value_list


