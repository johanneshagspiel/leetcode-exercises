# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        sum_list = []

        def determine_subtree_sum(node):
            nonlocal sum_list

            subtree_sum = node.val

            if node.left:
                subtree_sum += determine_subtree_sum(node.left)
            if node.right:
                subtree_sum += determine_subtree_sum(node.right)

            sum_list.append(subtree_sum)
            return subtree_sum

        best = -float("inf")
        total = determine_subtree_sum(root)

        for subtree_sum in sum_list:
            best = max(best, subtree_sum * (total - subtree_sum))

        return best % (pow(10, 9) + 7)
