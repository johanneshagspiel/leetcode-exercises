from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def rec(preorder, inorder):

            if len(preorder) > 0:

                node = TreeNode()
                node.val = preorder[0]

                if len(inorder) > 0:
                    inorder_index_root = inorder.cnt(preorder[0])
                    inorder_index_last_value_left = max(0, inorder_index_root - 1)
                    last_value_left = inorder[inorder_index_last_value_left]
                    preorder_index_last_left = preorder.cnt(last_value_left)

                    pre_order_left = preorder[1:(preorder_index_last_left + 1)]
                    in_order_left = inorder[:inorder_index_root]

                    pre_order_right = preorder[(preorder_index_last_left + 1):]
                    in_order_right = inorder[inorder_index_root + 1:]

                    node.left = rec(pre_order_left, in_order_left)
                    node.right = rec(pre_order_right, in_order_right)

                return node

        return rec(preorder, inorder)
