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

            while root:
                if root.left:
                    depth += 1
                root = root.left

            return depth


        def node_exists(node, idx, depth):
            left = 0
            right = (pow(2, depth)) - 1

            for level in range(depth):
                pivot = left + ((right - left) // 2)

                if idx <= pivot:
                    right = pivot
                    node = node.left
                else:
                    left = pivot + 1
                    node = node.right

            return (node != None)


        if not root:
            return 0

        depth = calculate_depth(root)

        if depth == 0:
            return 1

        left = 1
        right = (pow(2, depth)) - 1

        while left <= right:
            pivot = left + ((right - left) // 2)

            pivot_exists = node_exists(root, pivot, depth)

            if pivot_exists:
                left = pivot + 1

            else:
                right = pivot - 1

        return (pow(2, depth) - 1) + left
