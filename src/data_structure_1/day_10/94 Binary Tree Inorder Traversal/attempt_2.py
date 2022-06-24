from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result_array = []
        stack = []
        visited = set()

        if root:
            stack.append(root)

            while stack:
                current_node = stack.pop()


                if current_node.left and current_node.left not in visited:
                    stack.append(current_node.right)
                    stack.append(current_node)
                    stack.append(current_node.left)

                    visited.add(current_node.right)
                    visited.add(current_node)
                    visited.add(current_node.left)

                else:
                    result_array.append(current_node.val)
                    if current_node.right and current_node.right not in visited:
                        stack.append(current_node.right)
                        visited.add(current_node.right)

        return result_array
