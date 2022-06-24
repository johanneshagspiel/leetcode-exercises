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
            return []

        else:

            queue = collections.deque()
            queue.append(root)
            result_array = []

            while queue:
                current_level_array = []
                length_queue = len(queue)

                for element in range(length_queue):
                    current_node = queue.popleft()
                    current_level_array.append(current_node.val)
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)

                result_array.append(current_level_array)

            return result_array
