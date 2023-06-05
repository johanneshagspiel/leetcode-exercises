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

            stack = []
            stack.append(root)
            previous = root
            left = False

            while stack:
                node = stack.pop()

                if node:
                    previous = node

                    if node.val > val:
                        stack.append(node.left)
                        left = True

                    else:
                        stack.append(node.right)
                        left = False

            if left:
                previous.left = TreeNode(val)
            else:
                previous.right = TreeNode(val)

            return root


