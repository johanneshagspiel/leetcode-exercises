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
            root = TreeNode(val=val)
        else:
            current_node = root

            while current_node:
                if current_node.val > val:
                    if not current_node.left:
                        current_node.left = TreeNode(val=val)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = TreeNode(val=val)
                        break
                    else:
                        current_node = current_node.right

        return root

