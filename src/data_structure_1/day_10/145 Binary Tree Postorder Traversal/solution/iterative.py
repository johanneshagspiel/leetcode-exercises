class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result_list = []
        stack = [root]

        while stack:

            current_node = stack.pop()

            result_list.append(current_node.val)
            stack.append(current_node.left)
            stack.append(current_node.right)

        return result_list[::-1]