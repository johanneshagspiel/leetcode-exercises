from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        seen = set()
        stack.append(root)
        result_list = []

        while stack:
            node = stack.pop()

            if node.left and node.left not in seen and node.right and node.right not in seen:
                stack.append(node)
                stack.append(node.right)
                stack.append(node.left)

            elif node.left and node.left not in seen:
                stack.append(node)
                stack.append(node.left)

            elif node.right and node.right not in seen:
                stack.append(node)
                stack.append(node.right)

            else:
                seen.add(node)
                result_list.append(node.val)

        return result_list
