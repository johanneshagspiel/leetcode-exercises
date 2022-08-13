from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        else:

            previous = root
            node = root
            left = False

            while node:
                previous = node
                if node.val > val:
                    node = node.left
                    left = True

                else:
                    node = node.right
                    left = False

            if left:
                previous.left = TreeNode(val)
            else:
                previous.right = TreeNode(val)

            return root
