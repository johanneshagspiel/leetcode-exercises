# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def calculate_depth(root):
            depth = 0

            while root.left:
                root = root.left
                depth += 1

            return depth

        def node_exists(depth, idx, node):
            left = 0
            right = pow(2, depth) - 1

            for level in range(depth):
                pivot = left + ((right - left) // 2)

                if idx > pivot:
                    node = node.right
                    left = pivot + 1
                else:
                    node = node.left
                    right = pivot - 1

            return node is not None

        if not root:
            return 0

        depth = calculate_depth(root)

        if depth == 0:
            return 1

        left = 1
        right = pow(2, depth) - 1

        while left <= right:
            pivot = left + ((right - left) // 2)

            checked_node = node_exists(depth, pivot, root)

            if checked_node:
                left = pivot + 1
            else:
                right = pivot - 1

        node_count = pow(2, depth) - 1 + left

        return node_count
