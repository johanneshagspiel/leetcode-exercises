# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_sum = -float("inf")

        def find_max_path(node, parent_val, parent_list):

            nonlocal max_sum

            cur_val = parent_val + node.val
            parent_list.append(cur_val)

            left_list = []
            if node.left:
                left_list = find_max_path(node.left, 0, left_list)

            right_list = []
            if node.right:
                right_list = find_max_path(node.right, 0, right_list)

            max_left = 0
            for entry in left_list:
                max_left = max(max_left, entry)
                comb_val = entry + cur_val
                parent_list.append(comb_val)

            max_right = 0
            for entry in right_list:
                max_right = max(max_right, entry)
                comb_val = entry + cur_val
                parent_list.append(comb_val)

            comb_sum = 0
            if max_left > 0:
                comb_sum += max_left
            if max_right > 0:
                comb_sum += max_right
            comb_sum += node.val

            max_sum = max(max_sum, comb_sum)

            return parent_list

        find_max_path(root, 0, [])

        return max_sum
