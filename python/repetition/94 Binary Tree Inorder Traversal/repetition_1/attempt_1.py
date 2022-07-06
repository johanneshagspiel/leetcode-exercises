import collections
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        value_list = []

        stack = []
        stack.append(root)

        seen = set()

        while stack:
            node = stack.pop()

            if node and node not in seen:
                if node.left and node.left not in seen:
                    stack.append(node.right)
                    stack.append(node)
                    stack.append(node.left)
                else:
                    seen.add(node)
                    value_list.append(node.val)
                    stack.append(node.right)

        return value_list
