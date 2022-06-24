# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        else:
            in_right_sub_tree = (root == q) or (self.search_subtree(root.right, q))
            in_left_sub_tree = (root == p) or (self.search_subtree(root.left, p))

            if in_left_sub_tree and in_right_sub_tree:
                return root
            elif in_left_sub_tree and not in_right_sub_tree:
                return self.lowestCommonAncestor(root.left, p, q)
            elif not in_left_sub_tree and in_right_sub_tree:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return None

    def search_subtree(self, root, node):
        if not root:
            return False
        elif root == node:
            return True
        else:
            return self.search_subtree(root.left, node) or self.search_subtree(root.right, node)
