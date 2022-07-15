import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result_list = []

        if not root:
            return result_list

        queue = collections.deque()
        queue.append(root)

        while queue:

            queue_len = len(queue)

            for element in range(queue_len):
                node = queue.popleft()

                if element == 0:
                    result_list.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return result_list
