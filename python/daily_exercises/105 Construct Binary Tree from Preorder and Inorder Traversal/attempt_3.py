from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.pre_order_index = 0
        self.inorder_dic = {}

        def create_tree(left, right):

            if left > right:
                return None

            node = TreeNode()
            node.val = preorder[self.pre_order_index]
            self.pre_order_index += 1

            node.left = create_tree(left, self.inorder_dic[node.val] - 1)
            node.right = create_tree(self.inorder_dic[node.val] + 1, right)
            return node


        for index, value in enumerate(inorder):
            self.inorder_dic[value] = index

        return create_tree(0, len(preorder) - 1)
