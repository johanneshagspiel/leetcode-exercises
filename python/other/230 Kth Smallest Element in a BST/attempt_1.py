from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return None

        arr = []

        def rec_in(node):
            if node:
                rec_in(node.left)
                arr.append(node.val)
                rec_in(node.right)

        rec_in(root)
        return arr[k]

