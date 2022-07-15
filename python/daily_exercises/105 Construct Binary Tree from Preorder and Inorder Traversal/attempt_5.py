from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.pre_order_pointer = 0
        self.inorder_dic = {}

        def create_tree(left, right):
            if left > right:
                return None

            root = TreeNode()
            root.val = preorder[self.pre_order_pointer]
            self.pre_order_pointer += 1

            root.left = create_tree(left, self.inorder_dic[root.val] - 1)
            root.right = create_tree(self.inorder_dic[root.val] + 1, right)
            return root

        for index, value in enumerate(inorder):
            self.inorder_dic[value] = index

        return create_tree(0, len(preorder) - 1)
        