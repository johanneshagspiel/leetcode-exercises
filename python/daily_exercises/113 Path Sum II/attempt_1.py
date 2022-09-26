from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        res = []

        stack = []
        stack.append((root, 0, []))

        while stack:
            node, path_sum, path_list = stack.pop()

            path_sum += node.val
            path_list.append(node.val)

            if not node.left and not node.right:
                if path_sum == targetSum:
                    res.append(path_list)

            else:
                if node.left:
                    stack.append((node.left, path_sum, path_list.copy()))

                if node.right:
                    stack.append((node.right, path_sum, path_list.copy()))

        return res
