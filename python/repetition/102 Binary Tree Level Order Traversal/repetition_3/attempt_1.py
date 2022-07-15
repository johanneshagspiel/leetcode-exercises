from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result_list = []

        def rec_inorder(index, node):
            if node:
                if index > len(result_list):
                    result_list.append([])

                result_list[index].append(node.val)
                rec_inorder(index+1, node.left)
                rec_inorder(index+1, node.right)

        rec_inorder(1, root)
        return result_list

