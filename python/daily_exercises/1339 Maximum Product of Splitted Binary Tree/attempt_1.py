    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


    class CombinedNode:
        def __init__(self, treeNode):
            self.val = treeNode.val
            self.left = treeNode.left
            self.right = treeNode.right
            self.combinedVal = 0


    class Solution:
        def maxProduct(self, root: Optional[TreeNode]) -> int:

            def determine_combined_val(node):
                combinedVal = node.val

                if node.left:
                    combinedVal += determine_combined_val(node.left)
                if node.right:
                    combinedVal += determine_combined_val(node.right)

                node.combinedVal = combinedVal
                return combinedVal

            if not root:
                return 0

            rootCombined = CombinedNode(root)

            stack = [rootCombined]

            while stack:
                combinedNode = stack.pop()

                if combinedNode.right:
                    right_combined_node = CombinedNode(combinedNode.right)
                    combinedNode.right = right_combined_node
                    stack.append(right_combined_node)

                if combinedNode.left:
                    left_combined_node = CombinedNode(combinedNode.left)
                    combinedNode.left = left_combined_node
                    stack.append(left_combined_node)

            determine_combined_val(rootCombined)

            max_sum = -float("inf")

            root_combined_val = rootCombined.combinedVal
            stack = [rootCombined]

            while stack:
                node = stack.pop()

                node_combined_val = node.combinedVal

                if node.right:
                    right_node_combined_val = node.right.combinedVal
                    other_tree_val = root_combined_val - right_node_combined_val
                    combined_product = right_node_combined_val * other_tree_val
                    max_sum = max(max_sum, combined_product)
                    stack.append(node.right)

                if node.left:
                    left_node_combined_val = node.left.combinedVal
                    other_tree_val = root_combined_val - left_node_combined_val
                    combined_product = left_node_combined_val * other_tree_val
                    max_sum = max(max_sum, combined_product)
                    stack.append(node.left)

            return max_sum % (pow(10, 9) + 7)
