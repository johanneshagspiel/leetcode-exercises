from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        else:

            stack = []
            stack.append(root)

            while stack:
                current_node = stack.pop()
                current_value = current_node.val

                if current_value == val:
                    return current_node
                elif current_value < val:
                    stack.append(current_node.right)
                else:
                    stack.append(current_node.left)
