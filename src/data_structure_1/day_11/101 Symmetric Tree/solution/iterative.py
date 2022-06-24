import collections
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        else:
            queue = collections.deque()
            queue.append(root)
            queue.append(root)

            while queue:
                left_node = queue.popleft()
                right_node = queue.popleft()

                if not left_node and not right_node:
                    continue
                elif left_node.val != right_node.val:
                    return False
                elif (left_node and not right_node) or (not left_node and right_node):
                    return False
                else:
                    queue.append(left_node.left)
                    queue.append(right_node.right)
                    queue.append(left_node.right)
                    queue.append(right_node.left)

            return True