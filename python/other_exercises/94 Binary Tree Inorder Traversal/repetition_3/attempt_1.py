from typing import Optional,List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result_list = []
        seen = set()
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node:
                if node.left and node.left not in seen:
                    stack.append(node.right)
                    stack.append(node)
                    stack.append(node.left)

                elif node not in seen:
                    seen.add(node)
                    result_list.append(node.val)
                    stack.append(node.right)

        return result_list

