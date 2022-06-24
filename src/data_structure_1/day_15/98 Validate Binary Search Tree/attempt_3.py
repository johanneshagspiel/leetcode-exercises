class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):

            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev_node:
                return False
            self.prev_node = root.val
            return inorder(root.right)

        self.prev_node = -math.inf
        return inorder(root)
