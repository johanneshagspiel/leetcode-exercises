from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        else:
            self.left_array =[]
            self.pre_order_recursive(root.left)

            self.right_array = []
            self.test_recursive(root.right)

            if len(self.left_array) != len(self.right_array):
                return False

            else:
                for index in range(len(self.left_array)):
                    left_value = self.left_array[index]
                    right_value = self.right_array[index]

                    if left_value != right_value:
                        return False

                return True


    def pre_order_recursive(self, root):

        if root:
            self.left_array.append(root.val)
            self.pre_order_recursive(root.left)
            self.pre_order_recursive(root.right)
        else:
            self.left_array.append(None)

    def test_recursive(self, root):

        if root:
            self.right_array.append(root.val)
            self.test_recursive(root.right)
            self.test_recursive(root.left)
        else:
            self.right_array.append(None)