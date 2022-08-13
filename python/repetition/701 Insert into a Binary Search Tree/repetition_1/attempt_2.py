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

            def rec(node, prev, left):
                if not node:
                    if left:
                        prev.left = TreeNode(val)
                    else:
                        prev.right = TreeNode(val)
                else:
                    if val > node.val:
                        rec(node.right, node, False)
                    else:
                        rec(node.left, node, True)

            rec(root, root, False)
            return root

