# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        else:
            result_array = []
            self.inorder_search(root, result_array)

            left_pointer, right_pointer = 0, len(result_array) - 1

            while left_pointer < right_pointer:
                combined_result = result_array[left_pointer] + result_array[right_pointer]

                if combined_result == k:
                    return True
                elif combined_result < k:
                    left_pointer += 1
                else:
                    right_pointer -= 1

            return False

    def inorder_search(self, root, result_array):

        if not root:
            return
        else:
            self.inorder_search(root.left, result_array)
            result_array.append(root.val)
            self.inorder_search(root.right, result_array)